# coding=utf-8

from heap import Heap
from param import HMMParameter

def viterbi(param, observations, path_num=1):
    assert(isinstance(param, HMMParameter))

    probs, states = {}, {}
    for state in param.statesof(observations[0]):
        probs[state] = [param.initial_prob(state) + param.emission(state, observations[0])]
        states[state] = {-len(observations): None}

    for i in range(1, len(observations)):
        for state in param.statesof(observations[i]):
            max_tuple = max(
                                [
                                    (probs[s][-1] + param.transtion(s, state) + param.emission(state, observations[i]), s) 
                                    for s in param.statesof(observations[i - 1])
                                ]
                            )
            probs[state] = probs.get(state, []) + [max_tuple[0]]
            states[state] = {**states.get(state, {}), (i - len(observations)): max_tuple[1]}
    
    last_states = param.statesof(observations[-1])
    heap = Heap(min(path_num, len(last_states)))
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
