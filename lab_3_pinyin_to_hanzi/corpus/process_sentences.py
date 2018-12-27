# coding=utf-8

import os
import sys
import json
import pypinyin

SENTENCES_FILE = "./sentences.txt"

EMISSION_FILE = "./emission.txt"
TRANSITION_FILE = "./transition.txt"
INITIAL_PROB_FILE = "./initial_prob.txt"

def process_sentences():
    emssion = {}
    transition = {}
    initial_prob = {}
    with open(SENTENCES_FILE, "r", encoding="utf8") as f:
        sentences = f.readlines()
        for sentence in sentences:
            pinyin = pypinyin.lazy_pinyin(sentence, errors="ignore")