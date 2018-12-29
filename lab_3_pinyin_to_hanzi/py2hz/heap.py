# coding=utf-8

import heapq

class Heap(object):
    def __init__(self, capacity):
        self._container = []
        self._capacity = capacity

    def push(self, key, value):
        heapq.heappush(self._container, (key, value))
        while len(self._container) > self._capacity:
            heapq.heappop(self._container)
    
    def pop(self):
        if len(self._container) > 0:
            return heapq.heappop(self._container)
        else:
            return None

    def __len__(self):
        return len(self._container)

    def __iter__(self):
        for item in self._container:
            yield item

    def __str__(self):
        string = ["["]
        for key, value in self._container:
            string.append("(" + str(key) + ", " + str(value) + ")")
        string.append("]")
        return "\n".join(string)

    def __repr__(self):
        return self.__str__()