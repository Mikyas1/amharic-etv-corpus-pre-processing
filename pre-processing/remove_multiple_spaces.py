import re
from utils.helpers import *

def replace_multiple_spaces(sentence):
    # Replace multiple spaces with a single space
    return re.sub(r'\s{2,}', ' ', sentence)


def main():
    args = arg_parser(description="""remove spacer like "      ", more than one with " " 
                                    (replace multiple spaces with single space)""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def replace_multiple_spaces_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), replace_multiple_spaces), args.output_file)
     
       
 
if __name__ == "__main__":
    main()