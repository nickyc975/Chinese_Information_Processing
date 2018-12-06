import sys

def eval_line(output_list, gold_list):
    correct_word_count = 0
    output_pos, gold_pos = 0, 0
    output_checked_len, gold_checked_len = 0, 0
    line_len = sum(map(lambda x: len(x), output_list))
    while output_checked_len < line_len or gold_checked_len < line_len:
        if output_checked_len + len(output_list[output_pos]) \
           == gold_checked_len + len(gold_list[gold_pos]):
            if output_checked_len == gold_checked_len:
                correct_word_count += 1

            if output_checked_len < line_len:
                output_checked_len += len(output_list[output_pos])
                if output_pos < len(output_list) - 1:
                    output_pos += 1

            if gold_checked_len < line_len:
                gold_checked_len += len(gold_list[gold_pos])
                if gold_pos < len(gold_list) - 1:
                    gold_pos += 1

        elif output_checked_len + len(output_list[output_pos]) \
             < gold_checked_len + len(gold_list[gold_pos]) \
             and output_checked_len < line_len:

            output_checked_len += len(output_list[output_pos])
            if output_pos < len(output_list) - 1:
                output_pos += 1

        elif gold_checked_len < line_len:
            gold_checked_len += len(gold_list[gold_pos])
            if gold_pos < len(gold_list) - 1:
                gold_pos += 1
    
    return correct_word_count

if __name__ == "__main__":
    gold_word_count = 0
    output_word_count = 0
    correct_word_count = 0
    with open(sys.argv[1], "r", encoding="utf8") as output:
        with open(sys.argv[2], "r", encoding="utf8") as gold:
            output_lines = output.readlines()
            gold_lines = gold.readlines()
            for i in range(0, len(output_lines)):
                output_list = output_lines[i].strip().split()
                gold_list = gold_lines[i].strip().split()
                gold_word_count += len(gold_list)
                output_word_count += len(output_list)
                correct_word_count += eval_line(output_list, gold_list)
                
    print(", ".join([
            "correct word count: " + str(correct_word_count), 
            "output word count: " + str(output_word_count), 
            "gold word count: " + str(gold_word_count), 
            "correctness rate: " + str(float(correct_word_count) / float(gold_word_count))
        ]))
