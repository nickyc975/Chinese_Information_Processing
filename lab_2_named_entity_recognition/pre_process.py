import re
import sys


def get_word_tag(word_len=int):
        if word_len == 1:
            return ["W"]
        else:
            return ["W_B"] + ["W_I"] * (word_len - 2) + ["W_E"]


def get_p_o_s_tag(p_o_s=str, word_len=int):
        if word_len == 1:
            return [p_o_s]
        else:
            return [p_o_s + "_B"] + [p_o_s + "_I"] * (word_len - 2) + [p_o_s + "_E"]


def format_line(line=str):
    def merge_multiword(match_obj):
        return re.sub(r"/\w+ *", "", match_obj.group().strip("[]")) + "/"

    striped = re.sub(r"\d{8}-\d{2}-\d{3}-\d{3}/m ", "", line.strip())
    return re.sub(r"\[[^\[\]]+\]", merge_multiword, striped)


def tag_word(word=str):
    pair = word.split("/")
    word_len = len(pair[0])

    word_tag = []
    if pair[1] == "ns":
        word_tag = get_word_tag(word_len)
    else:
        word_tag = ["O"] * word_len

    p_o_s_tag = get_p_o_s_tag(pair[1], word_len)

    taged_word = []
    for i in range(word_len):
        taged_word.append("\t".join([pair[0][i], p_o_s_tag[i], word_tag[i]]) + "\n")
    return "".join(taged_word)


def pre_process(input_file, training_file, test_file):
    lines = input_file.readlines()
    for i in range(len(lines)):
        words = format_line(lines[i]).split()
        for word in words:
            if i % 5 == 0:
                test_file.write(tag_word(word))
            else:
                training_file.write(tag_word(word))


if __name__ == "__main__":
    input_file = open(sys.argv[1], "r", encoding="utf8")
    training_file = open(sys.argv[2], "w", encoding="utf8")
    test_file = open(sys.argv[3], "w", encoding="utf8")

    pre_process(input_file, training_file, test_file)

    input_file.close()
    training_file.close()
    test_file.close()
