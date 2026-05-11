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

            prompt = f"""Đưa ra 5 tiêu đề bài viết hấp dẫn và SEO-friendly dựa trên từ khóa: "{keyword}"

Yêu cầu:
- Tiêu đề phải có chứa từ khóa hoặc từ khóa liên quan
- Tiêu đề phải thu hút sự chú ý
- Độ dài: 50-70 ký tự
- Dùng tiếng Việt

Format trả về: Chỉ liệt kê 5 tiêu đề, mỗi tiêu đề trên một dòng, không có số thứ tự."""

            message = client.chat.completions.create(
                model="mixtral-8x7b-32768",
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
    try:
        data = request.json

        # Validate input
        website = data.get('website')
        title = data.get('title', '').strip()
        category = data.get('category', 'News').strip() or 'News'
        publish = data.get('publish', 'draft')

        if not website or website not in ['1', '2']:
            return jsonify({'error': 'Invalid website choice'}), 400

        if not title:
            return jsonify({'error': 'Title cannot be empty'}), 400

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

if __name__ == '__main__':
    print('\n' + '='*60)
    print('  DANG BAI WEB INTERFACE')
    print('='*60)
    print('\nTruy cập: http://localhost:5000')
    print('Nhấn Ctrl+C để dừng server\n')

    app.run(debug=True, port=5000)
