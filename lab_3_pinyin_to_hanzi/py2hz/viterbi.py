# coding=utf-8


import json
from limitedheap import LimitedHeap


class HMMParameter(object):
    def __init__(self, initail_prob_file, emission_file, transtion_file, pinyin2hanzi_file):
        self._initial_prob = json.load(open(initail_prob_file, "r", encoding="utf8"))
        self._emission = json.load(open(emission_file, "r", encoding="utf8"))
        self._transtion = json.load(open(transtion_file, "r", encoding="utf8"))
        self._pinyin2hanzi = json.load(open(pinyin2hanzi_file, "r", encoding="utf8"))

    def initial_prob(self, hanzi):
        return self._initial_prob.get(hanzi, 0)

    def emission(self, hanzi, pinyin):
        return self._emission.get(hanzi, {}).get(pinyin, 0)

    def transtion(self, from_hanzi, to_hanzi):
        return self._transtion.get(from_hanzi, {}).get(to_hanzi, 0)

    def statesof(self, pinyin):
        return set(self._pinyin2hanzi.get(pinyin, []))

    def states(self):
        return set(self._initial_prob.keys())

    def observations(self):
        return set(self._pinyin2hanzi.keys())


def viterbi(param, observations, path_num=1):
    assert(isinstance(param, HMMParameter))

    probs, states = {}, {}
    for state in param.statesof(observations[0]):
        probs[state] = [param.initial_prob(state) * param.emission(state, observations[0])]
        states[state] = {-len(observations): None}

    for i in range(1, len(observations)):
        for state in param.statesof(observations[i]):
            max_tuple = max(
                                [
                                    (probs[s][-1] * param.transtion(s, state) * param.emission(state, observations[i]), s) 
                                    for s in param.statesof(observations[i - 1])
                                ]
                            )
            probs[state] = probs.get(state, []) + [max_tuple[0]]
            states[state] = {**states.get(state, {}), (i - len(observations)): max_tuple[1]}
    
    last_states = param.statesof(observations[-1])
    heap = LimitedHeap(min(path_num, len(last_states)))
    for state in last_states:
        heap.push(probs[state][-1], state)

    results = []
    for item in heap:
        index = -1
        result = [item[1]]
        while index > -len(observations) and states[result[0]][index] is not None:
            result.insert(0, states[result[0]][index])
            index -= 1
        results.insert(0, result)
    return results
