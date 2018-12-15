import re
import sys


def format_line(line=str):
    def merge_multiword(match_obj):
        return re.sub(r"/\w+ *", "", match_obj.group().strip("[]")) + "/"

    striped = re.sub(r"\d{8}-\d{2}-\d{3}-\d{3}/m ", "", line.strip())
    return re.sub(r"\[[^\[\]]+\]", merge_multiword, striped)


def tag_word(word=str):
    [word, p_o_s] = word.split("/")
    word_len = len(word)

    word_tag = []
    if p_o_s == "ns":
        if word_len == 1:
            word_tag = ["W"]
        else:
            word_tag = ["W_B"] + ["W_I"] * (word_len - 2) + ["W_E"]
    else:
        word_tag = ["O"] * word_len

    p_o_s_tag = []
    if word_len == 1:
        p_o_s_tag = [p_o_s]
    else:
        p_o_s_tag = [p_o_s + "_B"] + [p_o_s + "_I"] * (word_len - 2) + [p_o_s + "_E"]

    taged_word = []
    for i in range(word_len):
        taged_word.append("\t".join([word[i], p_o_s_tag[i], word_tag[i]]) + "\n")
    return "".join(taged_word)


def pre_process(input_file, training_file, test_file):
    lines = input_file.readlines()
    for i in range(len(lines)):
        words = format_line(lines[i]).split()
        if i % 5 == 0:
            output_file = test_file
        else:
            output_file = training_file
        for word in words:
            output_file.write(tag_word(word))
        output_file.write("\n")


if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    training_file = open(sys.argv[2], "w")
    test_file = open(sys.argv[3], "w")

    pre_process(input_file, training_file, test_file)

    input_file.close()
    training_file.close()
    test_file.close()
