from utils.helpers import *

unique_pos = {}

def sentence_is_duplicate(pos):
    global unique_pos
    try:
        return unique_pos.get(pos, None)
    except Exception as e:
        return False


def unique_pos_wrapper(pos):
    _pos = pos.split(",")[-1]
    global unique_sentences
    existent_pos = sentence_is_duplicate(_pos)
    if existent_pos:
        print(_pos)
        return None
    try:
        unique_pos[_pos] = _pos
        return _pos
    except Exception as e:
        return None


def main():
    args = arg_parser(description="""Word pos""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def only_unique_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), unique_pos_wrapper), args.output_file)

if __name__ == "__main__":
    main()
