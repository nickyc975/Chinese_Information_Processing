import sys

def eval_file(input_file, tags):
    taged_cnt = 0
    should_tag_cnt = 0
    correct_tag_cnt = 0
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            [real_tag, taged_tag] = line.split("\t")[2:]
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
    try:
        with open(sys.argv[1], "r", encoding="utf16") as input_file:
            taged_cnt, should_tag_cnt, correct_tag_cnt = eval_file(input_file, ("W", "W_B", "W_I", "W_E"))
            print(" taged_cnt:          " + str(taged_cnt))
            print(" should_tag_cnt:     " + str(should_tag_cnt))
            print(" correct_tag_cnt:    " + str(correct_tag_cnt))
            print(" precision:          " + str(float(correct_tag_cnt) / float(taged_cnt)))
            print(" recall:             " + str(float(correct_tag_cnt) / float(should_tag_cnt)))
    except:
        print("Failed to open file!")
        print("Usage: python eval.py <file_name>")
