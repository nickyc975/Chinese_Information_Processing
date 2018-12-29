# coding=utf-8

import os
import sys
import pypinyin

PWD = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(PWD, "raw")
PINYIN_FILE = os.path.join(PWD, "pinyin.txt")
SENTENCES_FILE = os.path.join(PWD, "sentences.txt")

sys.path += [os.path.join(PWD, "..", "corpus")]
from process import extract_sentences

def gen_test():
    files = []
    for root, dirnames, filenames in os.walk(RAW_DIR):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(RAW_DIR, filename))

    processed_lines = []
    for raw in files:
        with open(raw, "r", encoding="utf8") as corpus:
            lines = corpus.readlines()
            for line in lines:
                processed_lines.extend(extract_sentences(line))

    pinyin_list = [" ".join(pypinyin.lazy_pinyin(line, errors="ignore")) for line in processed_lines]

    with open(PINYIN_FILE, "w", encoding="utf8") as pinyin_file:
        pinyin_file.write("\n".join(pinyin_list) + "\n")

    with open(SENTENCES_FILE, "w", encoding="utf8") as sentences_file:
        sentences_file.write("\n".join(processed_lines) + "\n")

if __name__ == "__main__":
    gen_test()
    