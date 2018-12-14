import re
import sys
import pickle


entities = {}


def extract_entities(line=str):
    def extract_entity(match_obj=str):
        match_obj = re.match(r"\{\{([a-z_]+): *([^\{\}]+) *\}\}", match_obj.group())
        key, value = match_obj.group(1), match_obj.group(2)
        if key in entities.keys():
            entities[key].append(value)
        else:
            entities[key] = [value]
        return value
    return re.sub(r"\{\{[a-z_]+: *[^\{\}]+ *\}\}", extract_entity, line)


if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="utf8") as input_file:
        with open(sys.argv[2], "w", encoding="utf8") as output_file:
            lines = input_file.readlines()
            for line in lines:
                output_file.write(extract_entities(line))

    for key, value in entities.items():
        entities[key] = set(value)
    
    pickle.dump(entities, open(sys.argv[3], "wb"))