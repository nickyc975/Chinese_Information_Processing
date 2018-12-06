#!/usr/bin/env python
import pickle
import sys


def max_match_segment(line, dic):
    words = []
    base, rear = 0, len(line)
    while base < len(line):
        for rear in range(len(line), base, -1):
            word = line[base:rear]
            if word in dic:
                break
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
            f.write("  ".join(max_match_segment(line.strip(), dic)) + "\n")

