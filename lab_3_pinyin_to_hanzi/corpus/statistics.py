# coding=utf-8

import os
import json

PWD = os.path.dirname(os.path.abspath(__file__))

SENTENCES_FILE = os.path.join(PWD, "sentences.txt")
OUTPUT_DIR = os.path.join(PWD, "..", "py2hz", "corpus")
EMISSION_FILE =  os.path.join(OUTPUT_DIR, "emission.json")
TRANSITION_FILE =  os.path.join(OUTPUT_DIR, "transition.json")
INITIAL_PROB_FILE =  os.path.join(OUTPUT_DIR, "initial_prob.json")
PINYIN2HANZI_FILE =  os.path.join(OUTPUT_DIR, "pinyin2hanzi.json")


def load_sentences(file_path):
    sentences = []
    with open(file_path, "r", encoding="utf8") as fp:
        lines = fp.readlines()
        for line in lines:
            sentence = line.strip("\n").split()
            sentences.append([tuple(pair.split("/")) for pair in sentence])
    return sentences


def statistics():
    emssion = {}
    transition = {}
    initial_prob = {}
    pinyin2hanzi = {}
    sentences = load_sentences(SENTENCES_FILE)
    for sentence in sentences:
        for hanzi, pinyin in sentence:
            if hanzi in emssion.keys():
                if pinyin in emssion[hanzi].keys():
                    emssion[hanzi][pinyin] += 1
                else:
                    emssion[hanzi][pinyin] = 1
            else:
                emssion[hanzi] = {pinyin: 1}
            
            if hanzi in initial_prob.keys():
                initial_prob[hanzi] += 1
            else:
                initial_prob[hanzi] = 1

            if pinyin in pinyin2hanzi.keys():
                pinyin2hanzi[pinyin].append(hanzi)
            else:
                pinyin2hanzi[pinyin] = [hanzi]
        
        for i in range(len(sentence) - 1):
            this_char = sentence[i][0]
            next_char = sentence[i + 1][0]
            if this_char in transition.keys():
                if next_char in transition[this_char].keys():
                    transition[this_char][next_char] += 1
                else:
                    transition[this_char][next_char] = 1
            else:
                transition[this_char] = {next_char: 1}

    total_char = sum(initial_prob.values())
    for key, value in initial_prob.items():
        initial_prob[key] = float(value) / total_char
    json.dump(initial_prob, open(INITIAL_PROB_FILE, "w", encoding="utf8"))

    for key, value in emssion.items():
        total_pinyin = sum(value.values())
        for k, v in value.items():
            value[k] = float(v) / total_pinyin
        emssion[key] = value
    json.dump(emssion, open(EMISSION_FILE, "w", encoding="utf8"))

    for key, value in transition.items():
        total_trans = sum(value.values())
        for k, v in value.items():
            value[k] = float(v) / total_trans
        transition[key] = value
    json.dump(transition, open(TRANSITION_FILE, "w", encoding="utf8"))

    for key, value in pinyin2hanzi.items():
        pinyin2hanzi[key] = list(set(value))
    json.dump(pinyin2hanzi, open(PINYIN2HANZI_FILE, "w", encoding="utf8"))


if __name__ == "__main__":
    statistics()
