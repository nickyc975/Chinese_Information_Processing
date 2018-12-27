# coding=utf-8

import os
import sys

def is_hanzi(s=str):
    return False if len(s) == 0 else all(u'\u4e00' <= c <= u'\u9fa5' or c == u'〇' for c in s)