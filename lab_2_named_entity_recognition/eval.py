import sys

def eval_file(input_file, tags):
    taged_cnt = 0
    should_tag_cnt = 0
    correct_tag_cnt = 0
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            [word, p_o_s, real_tag, taged_tag] = line.split("\t")
            if real_tag in tags and taged_tag in tags and real_tag == taged_tag:
                taged_cnt += 1
                should_tag_cnt += 1
                correct_tag_cnt += 1
            else:
                if real_tag in tags:
                    should_tag_cnt += 1

                if taged_tag in tags:
                    taged_cnt += 1
    return taged_cnt, should_tag_cnt, correct_tag_cnt



if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        taged_cnt, should_tag_cnt, correct_tag_cnt = eval_file(input_file, ("W", "W_B", "W_I", "W_E"))
        print(
            "taged_cnt: " + str(taged_cnt) + "\n",
            "should_tag_cnt: " + str(should_tag_cnt) + "\n",
            "correct_tag_cnt: " + str(correct_tag_cnt) + "\n",
            "correctness: " + str(float(correct_tag_cnt) / float(taged_cnt)) + "\n",
            "recall: " + str(float(correct_tag_cnt) / float(should_tag_cnt)) + "\n"
        )
            