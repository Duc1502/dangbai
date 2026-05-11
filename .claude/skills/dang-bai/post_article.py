#!/usr/bin/env python3
"""
Tu dong tao va dang bai viet len WordPress bang Groq AI + Stability AI images.
Cach dung:
  python src/post_article.py --title "Tieu de bai" --category "Technology"
"""
import os
import sys
import json
import argparse
import logging
import requests
import re
from datetime import datetime
from requests.auth import HTTPBasicAuth

# ── Get project root ──────────────────────────────────────────────────────────
def get_project_root():
    current = os.path.dirname(os.path.abspath(__file__))
    # Go up: dang-bai -> skills -> .claude -> root
    for _ in range(3):
        current = os.path.dirname(current)
    return current

PROJECT_ROOT = get_project_root()

# ── Load .env ──────────────────────────────────────────────────────────────────
def load_env():
    env_path = os.path.join(PROJECT_ROOT, '.env')
    if not os.path.exists(env_path):
        return
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value

load_env()

# ── Setup logging ──────────────────────────────────────────────────────────
def setup_logging():
    log_dir = os.path.join(PROJECT_ROOT, '.claude', 'skills', 'dang-bai', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f'post_article_{datetime.now().strftime("%Y%m%d")}.log')
    logging.basicConfig(
        level=getattr(logging, os.environ.get('LOG_LEVEL', 'INFO')),
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, encoding='utf-8'),
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# ── Load website config ────────────────────────────────────────────────────────
def load_websites():
    config_path = os.path.join(PROJECT_ROOT, 'websites.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    sites = {}
    for site in data['websites']:
        sites[str(site['id'])] = {
            'name': site['name'],
            'url': site['url'].rstrip('/'),
            'username': site['username'],
            'app_password': os.environ.get(site['app_password_env'], ''),
        }
    return sites

# ── Generate content with Groq AI ───────────────────────────────────────────
def generate_content(title, category):
    from groq import Groq

    api_key = os.environ.get('GROQ_API_KEY', '')
    if not api_key:
        logger.error('GROQ_API_KEY chua duoc set trong .env')
        sys.exit(1)

    logger.info(f'Dang tao noi dung cho: {title}')
    prompt = f"""Write a comprehensive, SEO-optimized blog article in HTML format with the following structure.

Title: {title}
Category: {category}
Language: English

IMPORTANT STRUCTURE REQUIREMENTS:
- Total length: 1500-2000 words
- Start with an engaging introductory paragraph
- Include 4-5 main sections, each starting with <h2>Section Title</h2>
- Within sections, use <h3> for subsections (include 1-2 subsections per section)
- End with <h2>Conclusion</h2> section
- Use <p>, <ul>, <li>, <strong>, <em> tags naturally
- Include keywords related to the title throughout
- Write in professional, engaging English

CRITICAL - DO NOT ADD NUMBERS TO HEADINGS:
- NEVER start h2 or h3 headings with numbers (e.g., "1.", "1.1.", "2.", etc.)
- Use simple descriptive titles without numbering
- Example WRONG: "<h2>1. Introduction</h2>"
- Example RIGHT: "<h2>Introduction</h2>"

FORMAT:
- Do NOT include <html>, <head>, <body> wrapper tags
- Do NOT include the title as <h1> (it will be added separately)
- Do NOT include any <hr> tags or dividers (they will be added automatically)
- Return ONLY the HTML content
- No markdown, no explanations, no code blocks
- Each paragraph should be wrapped in <p> tags

Return the complete HTML content now."""

    client = Groq(api_key=api_key)
    message = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        max_tokens=4096,
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.7,
    )
    content = message.choices[0].message.content
    logger.info(f'Noi dung da tao: {len(content)} ky tu')
    return content

# ── Load images from files ────────────────────────────────────────────────────
def load_images_from_files(image_paths):
    if not image_paths:
        return []

    images = []
    for image_path in image_paths:
        if not image_path or not os.path.exists(image_path):
            print(f'[load_images_from_files] WARNING - File not found: {image_path}')
            logger.warning(f'Image file not found: {image_path}')
            continue

        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
            print(f'[load_images_from_files] OK - Image loaded: {len(image_data)} bytes from {os.path.basename(image_path)}')
            logger.info(f'Loaded image from file: {image_path} ({len(image_data)} bytes)')
            images.append(image_data)
        except Exception as e:
            print(f'[load_images_from_files] WARNING - Failed to read file {image_path}: {e}')
            logger.warning(f'Failed to load image file {image_path}: {e}')
            continue

    return images

# ── Generate image with Stability AI ───────────────────────────────────────────
def generate_image(title, category):
    api_key = os.environ.get('STABILITY_API_KEY', '')
    if not api_key:
        print('[generate_image] ERROR - STABILITY_API_KEY not found in .env')
        logger.warning('STABILITY_API_KEY chua duoc set, bo qua anh')
        return None

    print(f'[generate_image] Starting image generation for: {title}')
    logger.info(f'Dang tao anh voi Stability AI: {title}')

    # Create prompt from title and category
    prompt = f"Professional blog featured image for article about '{title}' in {category} category. Modern design, high quality, professional, eye-catching, suitable for technology and business blog. 4K resolution."
    print(f'[generate_image] Prompt: {prompt[:100]}...')

    try:
        r = requests.post(
            'https://api.stability.ai/v2beta/stable-image/generate/core',
            headers={
                'authorization': f'Bearer {api_key}',
                'accept': 'image/*',
            },
            files={'none': ''},
            data={
                'prompt': prompt,
                'negative_prompt': 'blurry, low quality, watermark',
                'aspect_ratio': '16:9',
                'output_format': 'jpeg',
            },
            timeout=60
        )

        print(f'[generate_image] Response status: {r.status_code}')

        if r.status_code == 200:
            print(f'[generate_image] OK - Image generated successfully ({len(r.content)} bytes)')
            logger.info('Anh da tao thanh cong')
            return r.content
        elif r.status_code == 402:
            print(f'[generate_image] ERROR_402_CREDIT_EXHAUSTED - Stability AI API credit exhausted')
            logger.warning('Stability AI API credit exhausted')
            return None
        else:
            print(f'[generate_image] ERROR - API returned {r.status_code}: {r.text[:200]}')
            logger.warning(f'Tao anh that bai: {r.status_code} - {r.text[:200]}')
            return None
    except Exception as e:
        print(f'[generate_image] ERROR - Exception: {str(e)}')
        logger.error(f'Image generation exception: {str(e)}')
        return None

# ── Upload image to WordPress ──────────────────────────────────────────────────
def upload_image(image_data, title, auth, site_url, alt_text=''):
    filename = title[:40].lower().replace(' ', '-').replace('/', '-') + '.jpg'
    logger.info(f'Dang upload anh: {filename}')
    r = requests.post(
        f'{site_url}/wp-json/wp/v2/media',
        auth=auth,
        headers={
            'Content-Disposition': f'attachment; filename="{filename}"',
            'Content-Type': 'image/jpeg',
        },
        data=image_data,
        timeout=30
    )
    r.raise_for_status()
    media_data = r.json()
    media_id = media_data['id']
    media_url = media_data.get('source_url', '')
    logger.info(f'Upload anh thanh cong, media ID: {media_id}, URL: {media_url}')
    return media_id, media_url

# ── Extract heading structure for TOC ──────────────────────────────────────────
def extract_heading_structure(html_content):
    """Extract h2, h3, h4 headings with hierarchy"""
    h2_pattern = r'<h2[^>]*>(.*?)</h2>'
    h3_pattern = r'<h3[^>]*>(.*?)</h3>'
    h4_pattern = r'<h4[^>]*>(.*?)</h4>'

    h2_matches = [(m.start(), 'h2', re.sub('<[^>]+>', '', m.group(1))) for m in re.finditer(h2_pattern, html_content)]
    h3_matches = [(m.start(), 'h3', re.sub('<[^>]+>', '', m.group(1))) for m in re.finditer(h3_pattern, html_content)]
    h4_matches = [(m.start(), 'h4', re.sub('<[^>]+>', '', m.group(1))) for m in re.finditer(h4_pattern, html_content)]

    all_headings = sorted(h2_matches + h3_matches + h4_matches, key=lambda x: x[0])
    return all_headings

# ── Create TOC HTML with JavaScript ────────────────────────────────────────────
def create_table_of_contents(headings):
    if not headings:
        return ''

    toc_html = '''<div class="toc-wrapper" style="background: #E8F4F8; padding: 20px; margin: 20px 0; border-left: 4px solid #0073AA; border-radius: 4px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
    <div class="toc-header" style="font-weight: bold; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none; font-size: 16px; color: #333;" onclick="toggleTOC(this)">
        <span>Table of Contents</span>
        <span class="toc-toggle" style="font-size: 20px; color: #0073AA;">▲</span>
    </div>
    <div class="toc-content" style="max-height: 600px; overflow-y: auto; display: block; margin-top: 15px;">
'''

    h2_counter = 0
    h3_counter = 0

    for i, (_, level, text) in enumerate(headings):
        safe_id = re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')
        clean_text = re.sub(r'^\d+(\.\d+)?\s+', '', text)

        if level == 'h2':
            h2_counter += 1
            h3_counter = 0
            padding = '0'
            number = f'{h2_counter}. '
        elif level == 'h3':
            h3_counter += 1
            padding = '20px'
            number = f'{h2_counter}.{h3_counter} '
        else:
            padding = '40px'
            number = ''

        toc_html += f'<div style="padding-left: {padding}; margin: 8px 0; line-height: 1.8;"><a href="#{safe_id}" style="color: #0073AA; text-decoration: none;">{number}{clean_text}</a></div>\n'

    toc_html += '''    </div>
</div>

<script>
function toggleTOC(element) {
    const content = element.nextElementSibling;
    const toggle = element.querySelector('.toc-toggle');
    if (content.style.display === 'none') {
        content.style.display = 'block';
        toggle.textContent = '▲';
    } else {
        content.style.display = 'none';
        toggle.textContent = '▼';
    }
}

// Smooth scroll to headings
document.querySelectorAll('.toc-wrapper a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
</script>
'''
    return toc_html

# ── Add IDs to headings for TOC links ───────────────────────────────────────────
def add_heading_ids(html_content):
    """Add id attributes to all h2, h3, h4 headings"""
    pattern = r'<(h[234])([^>]*)>(.*?)</\1>'
    html_content = re.sub(pattern, lambda m: f'<{m.group(1)} id="{re.sub(r"[^\w\s-]", "", m.group(3).lower()).replace(" ", "-")}">{m.group(3)}</{m.group(1)}>', html_content)
    return html_content

# ── Add yellow divider before h2 headings ───────────────────────────────────────
def add_h2_dividers(html_content):
    """Add yellow divider before each h2 heading"""
    divider = '<div style="width: 40px; height: 10px; background-color: #FFAD00; margin: 20px 0;"></div>'
    pattern = r'(<h2[^>]*>)'
    html_content = re.sub(pattern, divider + r'\1', html_content)
    return html_content

# ── Insert multiple images throughout content ──────────────────────────────────
def insert_multiple_images(html_content, image_urls):
    """Insert images throughout the content before h2 headings"""
    if not image_urls:
        return html_content

    h2_count = 0
    img_index = 0
    pattern = r'<h2[^>]*>'

    def replacer(match):
        nonlocal h2_count, img_index
        h2_count += 1
        # Insert images before h2 headings starting from 3rd one, spreading them out
        if h2_count >= 3 and img_index < len(image_urls):
            # Insert image every 2 h2 headings
            if (h2_count - 3) % 2 == 0:
                img_html = f'<img src="{image_urls[img_index]}" alt="Article image" style="width: 100%; max-width: 800px; height: auto; margin: 20px 0; display: block; border-radius: 4px;">'
                img_index += 1
                return img_html + match.group(0)
        return match.group(0)

    html_content = re.sub(pattern, replacer, html_content)

    # If any images left, append them to the end
    while img_index < len(image_urls):
        html_content += f'<img src="{image_urls[img_index]}" alt="Article image" style="width: 100%; max-width: 800px; height: auto; margin: 20px 0; display: block; border-radius: 4px;">'
        img_index += 1

    return html_content

# ── Format content with date, IDs, dividers, TOC ────────────────────────────────
def format_html_content(title, content, category, embedded_image_urls=None):
    # Add IDs to headings
    content = add_heading_ids(content)

    # Extract heading structure
    headings = extract_heading_structure(content)

    # Create TOC
    toc_html = create_table_of_contents(headings)

    # Add dividers before h2
    content = add_h2_dividers(content)

    # Insert embedded images throughout content
    if embedded_image_urls:
        content = insert_multiple_images(content, embedded_image_urls)

    # Create date string
    now = datetime.now()
    date_str = now.strftime('%B %d, %Y')

    # Build final HTML
    final_html = f'<p style="color: #666; font-size: 14px; margin-bottom: 20px;">Updated: {date_str}</p>\n'
    final_html += toc_html
    final_html += content

    return final_html

# ── Get or create category ─────────────────────────────────────────────────────
def get_or_create_category(name, auth, site_url, allow_create=True):
    r = requests.get(
        f'{site_url}/wp-json/wp/v2/categories',
        params={'search': name},
        auth=auth,
        timeout=10
    )
    r.raise_for_status()
    for cat in r.json():
        if cat['name'].lower() == name.lower():
            logger.info(f'Tim thay category: {name} (ID: {cat["id"]})')
            return cat['id']

    # If not found and create not allowed, return None
    if not allow_create:
        logger.warning(f'Category {name} not found and creation not allowed')
        return None

    # Create new category
    r = requests.post(
        f'{site_url}/wp-json/wp/v2/categories',
        auth=auth,
        json={'name': name},
        timeout=10
    )
    r.raise_for_status()
    cat_id = r.json()['id']
    logger.info(f'Tao category moi: {name} (ID: {cat_id})')
    return cat_id

# ── Create WordPress post ──────────────────────────────────────────────────────
def create_post(title, content, category_ids, media_id, status, auth, site_url):
    # Handle both single ID (backward compatibility) and list of IDs
    if isinstance(category_ids, int):
        category_ids = [category_ids]
    elif category_ids is None:
        category_ids = []

    payload = {
        'title': title,
        'content': f'<!-- wp:html -->{content}<!-- /wp:html -->',
        'status': status,
        'categories': category_ids if category_ids else [],
    }
    if media_id:
        payload['featured_media'] = media_id

    logger.info('Dang tao post...')
    r = requests.post(
        f'{site_url}/wp-json/wp/v2/posts',
        auth=auth,
        json=payload,
        timeout=30
    )
    r.raise_for_status()
    post = r.json()
    return post['id'], post['link']

# ── Choose website interactively ───────────────────────────────────────────────
def choose_website(sites):
    print('\nChon website de dang bai:')
    for site_id in sorted(sites.keys()):
        site = sites[site_id]
        print(f'  {site_id}. {site["name"]:30} ({site["url"]})')
    while True:
        choice = input('\nBan chon (1/2): ').strip()
        if choice in sites:
            return choice
        print('Lua chon khong hop le, thu lai.')

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='Tu dong dang bai viet len WordPress')
    parser.add_argument('--title', '-t', required=True, help='Tieu de bai viet')
    parser.add_argument('--category', '-c', default='News', help='Ten category (mac dinh: News)')
    parser.add_argument('--draft', action='store_true', help='Luu nhap thay vi publish ngay')
    parser.add_argument('--images', '-i', help='Duong dan file anh (phan cach bang dau phay, neu khong co thi tu tao bang Stability AI)')
    args = parser.parse_args()

    status = 'draft' if args.draft else 'publish'
    sites = load_websites()

    print(f'\n{"="*60}')
    print(f'  DANG BAI TU DONG')
    print(f'{"="*60}')

    site_id = choose_website(sites)
    site = sites[site_id]

    print(f'\n  Web      : {site["name"]}')
    print(f'  Tieu de  : {args.title}')
    print(f'  Category : {args.category}')
    print(f'  Status   : {status}')
    print(f'{"="*60}\n')

    auth = HTTPBasicAuth(site['username'], site['app_password'])
    site_url = site['url']

    try:
        # Buoc 1: Tao noi dung
        print('\n[STEP 1] Generating content...')
        content = generate_content(args.title, args.category)
        print(f'[STEP 1] OK - Content generated: {len(content)} characters')

        # Buoc 2: Tao/load anh - anh dau lam featured, anh khac rhai trong bai
        print('\n[STEP 2] Processing images...')
        media_id = None
        embedded_media_urls = []
        api_credit_exhausted = False
        image_data_list = []

        # Check if user provided image files
        if args.images:
            print(f'[STEP 2] Loading images from files...')
            image_paths = [p.strip() for p in args.images.split(',')]
            image_data_list = load_images_from_files(image_paths)

        # If not enough images or no images, try to generate first one
        if len(image_data_list) == 0:
            print('[STEP 2] Generating image with Stability AI...')
            generated_image = generate_image(args.title, args.category)
            # Check if generation failed due to credit exhaustion
            if generated_image is None:
                api_credit_exhausted = True
                print('[STEP 2] ERROR_NEED_IMAGE_UPLOAD - Stability AI API credit exhausted, user must upload image')
                sys.exit(2)
            image_data_list.append(generated_image)

        # Upload images
        if image_data_list:
            print(f'[STEP 2] OK - {len(image_data_list)} image(s) ready')

            # First image as featured
            try:
                print('[STEP 2.1] Uploading featured image...')
                media_id, featured_url = upload_image(image_data_list[0], args.title, auth, site_url)
                print(f'[STEP 2.1] OK - Featured image uploaded: ID={media_id}')
            except Exception as e:
                print(f'[STEP 2.1] ERROR - Featured image upload failed: {e}')
                logger.warning(f'Upload featured image that bai: {e}')

            # Remaining images as embedded
            for idx, img_data in enumerate(image_data_list[1:], 1):
                try:
                    print(f'[STEP 2.{idx+1}] Uploading embedded image {idx}...')
                    _, media_url = upload_image(img_data, f'{args.title}-img{idx}', auth, site_url)
                    embedded_media_urls.append(media_url)
                    print(f'[STEP 2.{idx+1}] OK - Embedded image {idx} uploaded')
                except Exception as e:
                    print(f'[STEP 2.{idx+1}] WARNING - Embedded image {idx} upload failed: {e}')
                    logger.warning(f'Upload embedded image {idx} that bai: {e}')
        else:
            print('[STEP 2] WARNING - No images available')

        # Format with date, IDs, dividers, TOC, embedded images
        content = format_html_content(args.title, content, args.category, embedded_media_urls)

        # Buoc 3: Category
        category_ids = []
        category_names = [cat.strip() for cat in args.category.split(',') if cat.strip()]
        allow_create = len(category_names) == 1  # Only create new category if single category selected

        for cat_name in category_names:
            try:
                cat_id = get_or_create_category(cat_name, auth, site_url, allow_create=allow_create)
                if cat_id:
                    category_ids.append(cat_id)
                elif not allow_create:
                    # If multiple categories and one not found, still post but warn
                    print(f'[STEP 3] WARNING - Category "{cat_name}" not found in CMS')
                    logger.warning(f'Category {cat_name} not found')
            except Exception as e:
                print(f'[STEP 3] WARNING - Error processing category "{cat_name}": {e}')
                logger.warning(f'Khong the xu ly category {cat_name}: {e}')

        # Buoc 4: Tao post
        post_id, post_url = create_post(args.title, content, category_ids, media_id, status, auth, site_url)

        print(f'\n{"="*60}')
        print(f'  HOAN THANH!')
        print(f'{"="*60}')
        print(f'  Post ID : {post_id}')
        print(f'  URL     : {post_url}')
        print(f'{"="*60}\n')

    except Exception as e:
        logger.error(f'Loi: {e}', exc_info=True)
        print(f'\nLoi: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
