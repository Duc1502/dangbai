#!/usr/bin/env python3
"""
Skill handler cho /dang-bai
Hỏi user về web và title, rồi gọi post_article.py
"""
import subprocess
import sys
import os

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up: dang-bai -> skills -> .claude -> root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SKILL_DIR)))

def main():
    print('\n' + '='*60)
    print('  DANG BAI TU DONG')
    print('='*60)

    # Hỏi website
    print('\nChon website de dang bai:')
    print('  1. Tech Update Daily              (https://techupdatedaily.com)')
    print('  2. Discovering AI World           (https://discoveringaiworld.com)')

    while True:
        site_choice = input('\nBan chon (1/2): ').strip()
        if site_choice in ['1', '2']:
            break
        print('Lua chon khong hop le, thu lai.')

    # Hỏi title
    title = input('\nTieu de bai viet: ').strip()
    if not title:
        print('Tieu de khong the trong!')
        sys.exit(1)

    # Hỏi category (tùy chọn)
    category = input('Category (mac dinh: News): ').strip() or 'News'

    # Hỏi có publish ngay không
    publish = input('Publish ngay hay luu nap (ngay/nap, mac dinh: nap): ').strip().lower()
    draft_flag = '' if publish == 'ngay' else '--draft'

    # Gọi post_article.py (cùng folder với main.py)
    post_article_path = os.path.join(SKILL_DIR, 'post_article.py')
    cmd = [
        sys.executable,
        post_article_path,
        '--title', title,
        '--category', category,
    ]

    if draft_flag:
        cmd.append(draft_flag)

    # Change to project root before running
    os.chdir(PROJECT_ROOT)

    # Thêm website choice vào stdin
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, text=True)
    proc.stdin.write(site_choice + '\n')
    proc.stdin.close()
    proc.wait()

if __name__ == '__main__':
    main()
