# coding=utf-8

import os
import sys
import json
import pypinyin

SENTENCES_FILE = "./sentences.txt"

HANZI_SET_FILE = "./hanzi.txt"
PINYIN_SET_FILE = "./pinyin.txt"
PROCESSED_SENTENCES_FILE = "./processed_sentences.txt"


def hanzi2pinyin():
    hanzi_set = []
    pinyin_set = []
    processed_sentences = []
    with open(SENTENCES_FILE, "r", encoding="utf8") as fp:
        sentences = fp.readlines()
        for sentence in sentences:
            processed_sentence = []
            sentence = sentence.strip("\n")
            pinyin_list = pypinyin.lazy_pinyin(sentence, errors="ignore")
            for hanzi, pinyin in zip(sentence, pinyin_list):
                hanzi_set.append(hanzi)
                pinyin_set.append(pinyin)
                processed_sentence.append("/".join([hanzi, pinyin]))
            processed_sentences.append(" ".join(processed_sentence))
    hanzi_set = set(hanzi_set)
    pinyin_set = set(pinyin_set)
            
    with open(HANZI_SET_FILE, "w", encoding="utf8") as hanzi_set_file:
        hanzi_set_file.write("\n".join(hanzi_set) + "\n")

    with open(PINYIN_SET_FILE, "w", encoding="utf8") as pinyin_set_file:
        pinyin_set_file.write("\n".join(pinyin_set) + "\n")

    with open(PROCESSED_SENTENCES_FILE, "w", encoding="utf8") as processed_sentences_file:
        processed_sentences_file.write("\n".join(processed_sentences) + "\n")

if __name__ == "__main__":
    hanzi2pinyin()