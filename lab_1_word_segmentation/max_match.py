#!/usr/bin/env python
import sys
import pickle


def forward_max_match_segment(line, dic):
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


def backward_max_match_segment(line, dic):
    words = []
    base, rear = len(line), 0
    while base > 0:
        for rear in range(0, base):
            word = line[rear:base]
            if word in dic:
                break
        words.append(line[rear:base])
        base = rear
    words.reverse()
    return words


def bi_direction_max_match_segment(line, dic):
    forword = forward_max_match_segment(line, dic)
    backward = backward_max_match_segment(line, dic)
    if len(forword) < len(backward):
        return forword
    elif len(forword) > len(backward):
        return backward
    else:
        def count_single_char(words):
            count = 0
            for word in words:
                if len(word) == 1:
                    count += 1
            return count
        return forword if count_single_char(forword) < count_single_char(backward) else backward


if __name__=="__main__":
    max_match_segment = callable
    if sys.argv[1] == "-forward":
        max_match_segment = forward_max_match_segment
    elif sys.argv[1] == "-backward":
        max_match_segment = backward_max_match_segment
    elif sys.argv[1] == "-bi_direction":
        max_match_segment = bi_direction_max_match_segment
    else:
        print("unknown segment option: " + sys.argv[1])
        sys.exit(1)

    try:
        fpi=open(sys.argv[2], "r", encoding="utf8")
    except:
        print("failed to open file", file=sys.stderr)
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[3], "rb"))
    except:
        print("failed to load dict", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[4], "w", encoding="utf8") as f:
        for line in fpi:
            f.write("  ".join(max_match_segment(line.strip(), dic)) + "\n")

