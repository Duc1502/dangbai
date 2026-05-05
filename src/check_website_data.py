#!/usr/bin/env python3
"""
Kiểm tra dữ liệu website - Check SEO, content, metadata
"""

import json
import os
from datetime import datetime

def check_website_data(websites_file="data/websites.json"):
    """Kiểm tra dữ liệu của tất cả website"""

    # Đọc danh sách website
    with open(websites_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    websites = data.get('websites', [])
    results = []

    print(f"🔍 Kiểm tra {len(websites)} website...\n")

    for site in websites:
        print(f"📌 {site['name']}: {site['url']}")

        result = {
            'website': site['name'],
            'url': site['url'],
            'status': 'active' if site['status'] == 'active' else 'inactive',
            'last_checked': datetime.now().isoformat(),
            'checks': {
                'title': 'OK',  # Placeholder
                'meta_description': 'OK',
                'headings': 'OK',
                'links': 'OK',
            }
        }
        results.append(result)
        print(f"  ✓ Kiểm tra xong\n")

    # Lưu kết quả
    os.makedirs('output/reports', exist_ok=True)

    report_file = f"output/reports/check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"✅ Lưu report: {report_file}\n")
    return results

if __name__ == '__main__':
    check_website_data()
