from viterbi import HMMParameter, viterbi

INITIAL_PROB_FILE = "./corpus/initial_prob.json"
EMISSION_FILE = "./corpus/emission.json"
TRANSITION_FILE = "./corpus/transition.json"
PINYIN2HANZI_FILE = "./corpus/pinyin2hanzi.json"

param = HMMParameter(INITIAL_PROB_FILE, EMISSION_FILE, TRANSITION_FILE, PINYIN2HANZI_FILE)

# ['哈', '尔', '滨', '工', '业', '大', '学', '计', '算', '机', '科', '学', '与', '技', '术', '学', '院']
print(viterbi(param, ["ha", "er", "bin", "gong", "ye", "da", "xue", "ji", "suan", "ji", "ke", "xue", "yu", "ji", "shu", "xue", "yuan"], path_num=1))