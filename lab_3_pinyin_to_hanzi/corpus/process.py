# coding=utf-8

import os
import sys
import pypinyin

PWD = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(PWD, "raw")
SENTENCES_FILE = os.path.join(PWD, "sentences.txt")


def is_hanzi(s=str):
    if len(s) == 0:
        return False
    else:
        return all(u'\u4e00' <= c <= u'\u9fa5' or c == u'〇' for c in s)


def extract_sentences(line=str):
    sentences = []
    line = line.strip("\n").replace(" ", "")

    sentence = []
    for char in line:
        if is_hanzi(char):
            sentence.append(char)
        else:
            sentences.append("".join(sentence))
            sentence.clear()
    return [s for s in sentences if len(s) > 1]


def hanzi2pinyin(sentence=str):
    result = []
    sentence = sentence.strip("\n")
    pinyin_list = pypinyin.lazy_pinyin(sentence, errors="ignore")
    for hanzi, pinyin in zip(sentence, pinyin_list):
        result.append("/".join([hanzi, pinyin]))
    return "  ".join(result)


def process():
    files = []
    processed_lines = []
    for root, dirnames, filenames in os.walk(RAW_DIR):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(RAW_DIR, filename))

    for raw in files:
        with open(raw, "r", encoding="utf8") as corpus:
            lines = corpus.readlines()
            for line in lines:
                processed_lines.extend(extract_sentences(line))

    processed_lines = set(processed_lines)
    with open(SENTENCES_FILE, "w", encoding="utf8") as sentences:
        for line in processed_lines:
            sentences.write(hanzi2pinyin(line) + "\n")


if __name__ == "__main__":
    process()