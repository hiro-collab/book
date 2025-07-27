# scripts/update_readme.py

import os
import re

README_HEADER = """# 目指せ1000日記録プロジェクト：実装作業日記

このリポジトリは、自分の勉強ノートです。
「操る」「可視化する」「つなげる」ことをテーマに、
日々のプログラミングや考えたことを1000日かけて書き留めています。

---

📌 [記録用テンプレートはこちら](https://github.com/hiro-collab/book/blob/main/1000_days_prompt_script.md)

## 📅 各日の記録
"""

README_FOOTER = """

---

## 📖 思想・構想

📖 [思想の核・構想はこちら（book_concept.md）](https://github.com/hiro-collab/book/blob/main/book_concept.md)
"""

def find_day_files():
    files = []
    for fname in os.listdir("."):
        if re.match(r"Day\d{3}\.md", fname):
            files.append(fname)
    files.sort()
    return files

def make_day_links(files):
    links = []
    for f in files:
        day = f.replace(".md", "")
        links.append(f"- [{day}](https://github.com/hiro-collab/book/blob/main/{f})")
    return "\n".join(links)

def main():
    files = find_day_files()
    links = make_day_links(files)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(README_HEADER)
        f.write(links)
        f.write(README_FOOTER)

if __name__ == "__main__":
    main()
