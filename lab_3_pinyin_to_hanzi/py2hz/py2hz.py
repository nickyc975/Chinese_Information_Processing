import os
import sys
from viterbi import HMMParameter, viterbi

PWD = os.path.dirname(os.path.abspath(__file__))

CORPUS_DIR = os.path.join(PWD, "corpus")
INITIAL_PROB_FILE = os.path.join(CORPUS_DIR, "initial_prob.json")
EMISSION_FILE = os.path.join(CORPUS_DIR, "emission.json")
TRANSITION_FILE = os.path.join(CORPUS_DIR, "transition.json")
PINYIN2HANZI_FILE = os.path.join(CORPUS_DIR, "pinyin2hanzi.json")

param = HMMParameter(INITIAL_PROB_FILE, EMISSION_FILE, TRANSITION_FILE, PINYIN2HANZI_FILE)

def py2hz(pinyin, path_num=1):
    assert(path_num > 0)
    assert(isinstance(pinyin, (list, set, tuple)))

    results = viterbi(param, pinyin, path_num)
    return ["".join(result) for result in results]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("\n".join(py2hz(sys.argv[1].split())))
    elif len(sys.argv) == 3:
        print("\n".join(py2hz(sys.argv[1].split(), int(sys.argv[2]))))
    else:
        print(
            "Usage: python py2hz.py <pinyin> [path num]\n" +
            "Example:\n" + 
            "        > python py2hz.py 'ni hao'\n" +
            "        你好\n" +
            "        > python py2hz.py 'ni hao' 3\n" +
            "        你好\n" +
            "        你毫\n" +
            "        鲵颢\n"
        )
