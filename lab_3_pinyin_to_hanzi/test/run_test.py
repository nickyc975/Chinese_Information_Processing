# coding=utf-8

import os
import sys

PWD = os.path.dirname(os.path.abspath(__file__))

sys.path += [os.path.join(PWD, "..", "py2hz")]
from py2hz import py2hz

PINYIN_FILE = os.path.join(PWD, "pinyin.txt")
OUTPUT_FILE = os.path.join(PWD, "output.txt")
SENTENCES_FILE = os.path.join(PWD, "sentences.txt")


def run_py2hz():
    sentences = []
    with open(PINYIN_FILE, "r", encoding="utf8") as pinyin_file:
        for line in pinyin_file.readlines():
            sentences.append("\n".join(py2hz(line.split())))

    with open(OUTPUT_FILE, "w", encoding="utf8") as output_file:
        output_file.write("\n".join(sentences) + "\n")


def statistics():
    outputs = []
    with open(OUTPUT_FILE, "r", encoding="utf8") as output_file:
        outputs = output_file.readlines()

    sentences = []
    with open(SENTENCES_FILE, "r", encoding="utf8") as sentences_file:
        sentences = sentences_file.readlines()

    total = 0
    correct = 0
    for output, sentence in zip(outputs, sentences):
        for output_char, sentence_char in zip(output, sentence):
            if output_char == sentence_char:
                correct += 1
            total += 1
    print("precision: " + str(float(correct) / float(total)) + "\n")


if __name__ == "__main__":
    run_py2hz()
    statistics()