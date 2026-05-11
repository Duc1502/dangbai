#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web interface for /dang-bai skill
Run: python app.py
Then visit: http://localhost:5000
"""
import os
import subprocess
import sys
import tempfile
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Fix Unicode encoding on Windows
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__, template_folder='templates')

SKILL_DIR = os.path.join(os.path.dirname(__file__), '.claude', 'skills', 'dang-bai')
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/suggest-titles', methods=['POST'])
def suggest_titles():
    try:
        data = request.json
        keyword = data.get('keyword', '').strip()

        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400

        # Try using Groq API for title suggestions
        try:
            from groq import Groq

            api_key = os.getenv('GROQ_API_KEY')
            if not api_key:
                return jsonify({'error': 'GROQ_API_KEY not configured in .env'}), 500

            client = Groq(api_key=api_key)

            prompt = f"""Generate 5 compelling and SEO-friendly blog post titles based on the keyword: "{keyword}"

Requirements:
- Titles must contain the keyword or related keywords
- Titles must be attention-grabbing and engaging
- Length: 50-70 characters
- Use English language

Format: List only 5 titles, one per line, no numbering or bullets."""

            message = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                max_tokens=300,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Parse response
            titles = message.choices[0].message.content.strip().split('\n')
            titles = [t.strip() for t in titles if t.strip()][:5]

            return jsonify({
                'success': True,
                'titles': titles
            })

        except ImportError:
            return jsonify({'error': 'Groq library not installed'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/post-article', methods=['POST'])
def post_article():
    temp_image_paths = []
    try:
        # Get form data and files
        website = request.form.get('website')
        title = request.form.get('title', '').strip()
        category = request.form.get('category', 'News').strip() or 'News'
        publish = request.form.get('publish', 'draft')
        image_files = request.files.getlist('images')

        if not website or website not in ['1', '2']:
            return jsonify({'error': 'Invalid website choice'}), 400

        if not title:
            return jsonify({'error': 'Title cannot be empty'}), 400

        # Save uploaded images to temp files if provided
        if image_files:
            try:
                temp_dir = tempfile.gettempdir()
                for image_file in image_files:
                    if image_file and image_file.filename:
                        temp_path = os.path.join(temp_dir, 'dang_bai_' + image_file.filename)
                        image_file.save(temp_path)
                        temp_image_paths.append(temp_path)
            except Exception as e:
                return jsonify({'error': f'Failed to save images: {str(e)}'}), 400

        # Run post_article.py
        post_article_path = os.path.join(SKILL_DIR, 'post_article.py')

        cmd = [
            sys.executable,
            post_article_path,
            '--title', title,
            '--category', category,
        ]

        if publish == 'draft':
            cmd.append('--draft')

        if temp_image_paths:
            cmd.extend(['--images', ','.join(temp_image_paths)])

        os.chdir(PROJECT_ROOT)

        # Run with website choice via stdin
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = proc.communicate(input=website + '\n', timeout=300)

        if proc.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Article posted successfully!',
                'output': stdout
            })
        elif proc.returncode == 2:
            return jsonify({
                'success': False,
                'error': 'Stability AI API credit exhausted. Please upload image to continue.',
                'error_type': 'NEED_IMAGE_UPLOAD',
                'output': stdout
            }), 402
        else:
            return jsonify({
                'success': False,
                'error': stderr or 'Unknown error',
                'output': stdout
            }), 500

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Process timeout (5 minutes)'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up temp image files
        for temp_path in temp_image_paths:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass

if __name__ == '__main__':
    print('\n' + '='*60)
    print('  DANG BAI WEB INTERFACE')
    print('='*60)
    print('\nTruy cập: http://localhost:5000')
    print('Nhấn Ctrl+C để dừng server\n')

    app.run(debug=True, port=5000)
