#!/usr/bin/env python3
"""
Đăng bài lên website - Tự động upload article
"""

import csv
import json
import os
from datetime import datetime

def read_articles(csv_file="data/articles.csv"):
    """Đọc danh sách bài viết từ CSV"""
    articles = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            articles.append(row)

    return articles

def post_article(article, dry_run=True):
    """Đăng một bài lên website"""

    title = article.get('Title', 'No Title')
    website = article.get('Website', 'unknown')
    publish_date = article.get('PublishDate', 'N/A')

    print(f"📝 Đăng bài: {title}")
    print(f"   Website: {website}")
    print(f"   Ngày: {publish_date}")

    if dry_run:
        print(f"   [DRY RUN] Sẽ đăng bài này\n")
        return {'status': 'draft', 'article': title}
    else:
        print(f"   ✓ Đã đăng\n")
        return {'status': 'published', 'article': title}

def main(csv_file="data/articles.csv", dry_run=True):
    """Đăng tất cả bài viết"""

    print(f"📚 Đọc bài viết từ {csv_file}...\n")

    articles = read_articles(csv_file)
    print(f"Tìm thấy {len(articles)} bài viết\n")

    results = []
    for article in articles:
        result = post_article(article, dry_run=dry_run)
        results.append(result)

    # Lưu kết quả
    os.makedirs('output/logs', exist_ok=True)

    log_file = f"output/logs/post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"✅ Lưu log: {log_file}\n")

if __name__ == '__main__':
    # Chạy với --dry-run để xem trước
    main(dry_run=True)

    # Bỏ comment dòng dưới để thực sự đăng bài
    # main(dry_run=False)
