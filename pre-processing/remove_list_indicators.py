import re
from utils.helpers import *

def remove_list_indicators(text):
    # Pattern to match ordered and unordered list indicators
    pattern = r'^\s*(?:\d+\.\s*|•\s*)'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text.strip()


def main():
    args = arg_parser(description="""Remove lists (starting with 1. 2. 3. .... or • ) 
                                  from sentences""", 
                                  input_dict=standard_input_output_args,)
    
    @with_info
    def remove_list_indicators_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(
                                            args.input_file), 
                                            remove_list_indicators
                                        ), 
                            args.output_file)


if __name__ == "__main__":
    main()
