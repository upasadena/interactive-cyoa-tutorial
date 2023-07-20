"""
# count_words.py
A cross-platform solution to `word_count.sh`

# Acknowledgements
This code comes from:
https://jackmckew.dev/counting-words-with-python.html
"""

# Imports
import os
import re
import pathlib
import io
import glob
from typing import List

DEBUG = False

# Source: https://github.com/gandreadis/markdown-word-count
def count_words_in_markdown(filePath: str):
    with open(filePath, "r", encoding="utf8") as f:
        text = f.read()

    # Comments
    text = re.sub(r"<!--(.*?)-->", "", text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace("\t", "    ")
    # More than 1 space to 4 spaces
    text = re.sub(r"[ ]{2,}", "    ", text)
    # Footnotes
    text = re.sub(r"^\[[^]]*\][^(].*", "", text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r"^( {4,}[^-*]).*", "", text, flags=re.MULTILINE)
    # Replace newlines with spaces for uniform handling
    text = text.replace("\n", " ")
    # Custom header IDs
    text = re.sub(r"{#.*}", "", text)
    # Remove images
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # Remove HTML tags
    text = re.sub(r"</?[^>]*>", "", text)
    # Remove special characters
    text = re.sub(r"[#*`~\-–^=<>+|/:]", "", text)
    # Remove footnote references
    text = re.sub(r"\[[0-9]*\]", "", text)
    # Remove enumerations
    text = re.sub(r"[0-9#]*\.", "", text)

    return len(text.split())

def count_words_in_dir(
    top_dir: str = "",
    excluded_dirs: List = [],
    debug: bool = False
) -> int:
    all_markdown: List  = []

    # Iterate through all files using pathlib
    files = glob.glob(f"{top_dir}**/*.md", recursive=True)

    for d in excluded_dirs:
        files = [x for x in files if not x.startswith(f"{top_dir}{d}")]
    
    for single_file in files:
        all_markdown.append(single_file)

    if debug:
        for f in files:
            print(f"debug: file '{f}'")
        # print(f"debug: all_markdown = '{all_markdown}'")

    total_word_count_markdown: int = 0
    for single_file in files:
        total_word_count_markdown += count_words_in_markdown(single_file)
    
    return total_word_count_markdown

def get_tut_words(debug=True) -> int:
    return count_words_in_dir("", [
        ".github\\",
        ".vscode\\",
        "scripts\\",
        "site\\",
        "venv\\",
    ], debug)

if __name__ == "__main__":
    tut_words = get_tut_words(debug=DEBUG)
    print(tut_words)
    # print(f"_Words: {tut_words:,}_")
    # input("Enter to exit: ? ")