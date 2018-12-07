#!/usr/bin/env python
import sys
import time
import pickle


def forward_max_match_segment(line, dic):
    """
    Forward maximum matching segmentation.

    :param line: line of text to segment.
    :param dic: dictionary.
    """
    words = []
    head, rear = 0, len(line)
    while head < len(line):
        for rear in range(len(line), head, -1):
            word = line[head:rear]
            if word in dic:
                break
        words.append(line[head:rear])
        head = rear
    return words


def backward_max_match_segment(line, dic):
    """
    Backward maximum matching segmentation.

    :param line: line of text to segment.
    :param dic: dictionary.
    """
    words = []
    head, rear = 0, len(line)
    while rear > 0:
        for head in range(0, rear):
            word = line[head:rear]
            if word in dic:
                break
        words.insert(0, line[head:rear])
        rear = head
    return words


def bi_direction_max_match_segment(line, dic):
    """
    Bi-direction maximum matching segmentation.

    :param line: line of text to segment.
    :param dic: dictionary.
    """
    forword = forward_max_match_segment(line, dic)
    backward = backward_max_match_segment(line, dic)
    if len(forword) < len(backward):
        return forword
    elif len(forword) > len(backward):
        return backward
    else:
        def count_single_char(words):
            return sum(map(lambda word: 1 if len(word) == 1 else 0, words))
        return forword if count_single_char(forword) < count_single_char(backward) else backward


if __name__=="__main__":
    """
    Usage: python max_match.py [-forward | -backward | -bi_direction] <file to segment> <dictionary file> <output file>
    """
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
        start = time.time()
        for line in fpi:
            f.write("  ".join(max_match_segment(line.strip(), dic)) + "\n")
        print("Finished segmentation in %f seconds." % (time.time() - start))

