# coding=utf-8

import os
import sys
import pypinyin

PWD = os.path.dirname(os.path.abspath(__file__))

sys.path += [os.path.join(PWD, "..", "pinyin2hanzi")]
from py2hz import py2hz

PINYIN_FILE = os.path.join(PWD, "pinyin.txt")
OUTPUT_FILE = os.path.join(PWD, "output.txt")

def test():
    sentences = []
    with open(PINYIN_FILE, "r", encoding="utf8") as pinyin_file:
        for line in pinyin_file.readlines():
            sentences.append(py2hz(line.split()))

    with open(OUTPUT_FILE, "w", encoding="utf8") as output_file:
        output_file.write("\n".join(sentences) + "\n")


if __name__ == "__main__":
    test()