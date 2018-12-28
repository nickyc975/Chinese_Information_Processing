from viterbi import HMMParameter, viterbi

INITIAL_PROB_FILE = "./corpus/initial_prob.json"
EMISSION_FILE = "./corpus/emission.json"
TRANSITION_FILE = "./corpus/transition.json"
PINYIN2HANZI_FILE = "./corpus/pinyin2hanzi.json"

param = HMMParameter(INITIAL_PROB_FILE, EMISSION_FILE, TRANSITION_FILE, PINYIN2HANZI_FILE)

print(viterbi(param, ["zhong", "guo", "de", "kou", "hao", "shi", "ni", "hao"]))