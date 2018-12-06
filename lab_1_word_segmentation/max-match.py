#!/usr/bin/env python
import pickle
import sys


def max_match_segment(line, dic):
    base = 0
    words = []
    while base < len(line):
        rear = base + 1
        for pos in range(base + 1, len(line)):
            word = line[base:pos]
            if word in dic:
                rear = pos
        words.append(line[base:rear])
        base = rear
    return words


if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r", encoding="utf8")
    except:
        print("failed to open file", file=sys.stderr)
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[2], "rb"))
    except:
        print("failed to load dict", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[3], "w", encoding="utf8") as f:
        for line in fpi:
            f.write("\t".join(max_match_segment(line.strip(), dic)) + "\n")

