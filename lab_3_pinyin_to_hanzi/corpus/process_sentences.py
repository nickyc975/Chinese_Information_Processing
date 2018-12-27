# coding=utf-8

import os
import sys
import json
import pypinyin

sys.path += [".."]
import pinyin2hanzi.utils as utils

SENTENCES_FILE = "./sentences.txt"

OUTPUT_DIR = "../pinyin2hanzi/corpus/"
EMISSION_FILE = OUTPUT_DIR + "emission.json"
TRANSITION_FILE = OUTPUT_DIR + "transition.json"
INITIAL_PROB_FILE = OUTPUT_DIR + "initial_prob.json"

def process_sentences():
    emssion = {}
    transition = {}
    initial_prob = {}
    with open(SENTENCES_FILE, "r", encoding="utf8") as f:
        sentences = f.readlines()
        for sentence in sentences:
            sentence = sentence.strip("\n\t ")
            if len(sentence) <= 1:
                continue

            pinyin = pypinyin.lazy_pinyin(sentence, errors="ignore")
            last_index = len(pinyin) - 1
            for i in range(last_index):
                if sentence[i] in initial_prob.keys():
                    initial_prob[sentence[i]] += 1
                else:
                    initial_prob[sentence[i]] = 1

                if sentence[i] in emssion.keys():
                    if pinyin[i] in emssion[sentence[i]].keys():
                        emssion[sentence[i]][pinyin[i]] += 1
                    else:
                        emssion[sentence[i]][pinyin[i]] = 1
                else:
                    emssion[sentence[i]] = {pinyin[i]: 1}
                
                if sentence[i] in transition.keys():
                    if sentence[i + 1] in transition[sentence[i]].keys():
                        transition[sentence[i]][sentence[i + 1]] += 1
                    else:
                        transition[sentence[i]][sentence[i + 1]] = 1
                else:
                    transition[sentence[i]] = {sentence[i + 1]: 1}
        
            if sentence[last_index] in initial_prob.keys():
                initial_prob[sentence[last_index]] += 1
            else:
                initial_prob[sentence[last_index]] = 1

            if sentence[last_index] in emssion.keys():
                if pinyin[last_index] in emssion[sentence[last_index]].keys():
                    emssion[sentence[last_index]][pinyin[last_index]] += 1
                else:
                    emssion[sentence[last_index]][pinyin[last_index]] = 1
            else:
                emssion[sentence[last_index]] = {pinyin[last_index]: 1}
    
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


if __name__ == "__main__":
    process_sentences()
