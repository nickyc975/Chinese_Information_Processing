# coding=utf-8

import json

class HMMParameter(object):
    def __init__(self, initail_prob_file, emission_file, transtion_file, pinyin2hanzi_file):
        self._initial_prob = json.load(open(initail_prob_file, "r", encoding="utf8"))
        self._emission = json.load(open(emission_file, "r", encoding="utf8"))
        self._transtion = json.load(open(transtion_file, "r", encoding="utf8"))
        self._pinyin2hanzi = json.load(open(pinyin2hanzi_file, "r", encoding="utf8"))

    def initial_prob(self, hanzi):
        return self._initial_prob.get(hanzi, float('-inf'))

    def emission(self, hanzi, pinyin):
        return self._emission.get(hanzi, {}).get(pinyin, float('-inf'))

    def transtion(self, from_hanzi, to_hanzi):
        return self._transtion.get(from_hanzi, {}).get(to_hanzi, float('-inf'))

    def statesof(self, pinyin):
        return set(self._pinyin2hanzi.get(pinyin, []))

    def states(self):
        return set(self._initial_prob.keys())

    def observations(self):
        return set(self._pinyin2hanzi.keys())