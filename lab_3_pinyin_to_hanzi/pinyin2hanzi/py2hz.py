import os
from viterbi import HMMParameter, viterbi

PWD = os.path.dirname(os.path.abspath(__file__))

CORPUS_DIR = os.path.join(PWD, "corpus")
INITIAL_PROB_FILE = os.path.join(CORPUS_DIR, "initial_prob.json")
EMISSION_FILE = os.path.join(CORPUS_DIR, "emission.json")
TRANSITION_FILE = os.path.join(CORPUS_DIR, "transition.json")
PINYIN2HANZI_FILE = os.path.join(CORPUS_DIR, "pinyin2hanzi.json")

param = HMMParameter(INITIAL_PROB_FILE, EMISSION_FILE, TRANSITION_FILE, PINYIN2HANZI_FILE)

# ['哈', '尔', '滨', '工', '业', '大', '学', '计', '算', '机', '科', '学', '与', '技', '术', '学', '院']
print(viterbi(param, ["ha", "er", "bin", "gong", "ye", "da", "xue", "ji", "suan", "ji", "ke", "xue", "yu", "ji", "shu", "xue", "yuan"], path_num=1))