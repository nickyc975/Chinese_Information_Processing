# coding=utf-8

import os
import sys

sys.path += [".."]
import pinyin2hanzi.utils as utils

RAW_DIR = "./raw"
SENTENCES_FILE = "./sentences.txt"


def extract_sentences(line=str):
    sentences = []
    line = line.strip("\n").replace(" ", "")

    sentence = []
    for char in line:
        if utils.is_hanzi(char):
            sentence.append(char)
        else:
            sentences.append("".join(sentence))
            sentence.clear()
    return [s for s in sentences if len(s) > 1]


def process_raw():
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
            sentences.write(line + "\n")

if __name__ == "__main__":
    process_raw()