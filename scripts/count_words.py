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

# Top directory to search through
# top_folder: pathlib.Path = pathlib.Path("../")
top_folder = "./docs/" # "../"

all_markdown: List  = []

# Folders to ignore
# Iterate through all files using pathlib
files = glob.glob(f"{top_folder}**/*.md", recursive=True)
# files = [x for x in files if not x.name.startswith("")]
for single_file in files:
    all_markdown.append(single_file)

# print(f"debug: all_markdown = '{all_markdown}'")

total_word_count_markdown: int = 0
for single_file in all_markdown:
    total_word_count_markdown += count_words_in_markdown(single_file)

print(total_word_count_markdown)