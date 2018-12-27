# coding=utf-8

import os
import sys

sys.path = sys.path + [".."]
import pinyin2hanzi.utils as utils

RAW_DIR = "./raw"
SENTENCES_FILE = "./sentences.txt"


def extract_sentences(line=str):
    sentences = []
    line = line.strip().replace(" ", "")

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
    for root, dirnames, filenames in os.walk(RAW_DIR):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(RAW_DIR, filename))

    with open(SENTENCES_FILE, "w", encoding="utf8") as sentences:
        for raw in files:
            with open(raw, "r", encoding="utf8") as corpus:
                lines = corpus.readlines()
                for line in lines:
                    sentences.write("\n".join(extract_sentences(line)) + "\n")


if __name__ == "__main__":
    process_raw()