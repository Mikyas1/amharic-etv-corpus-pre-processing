import re
from utils.helpers import *

def contains_latin_characters(sentence):
    return bool(re.search(r'[A-Za-z]', sentence))

def contains_latin_characters_wrapper(sentence):
    if contains_latin_characters(sentence=sentence):
        return None
    return sentence

def main():
    args = arg_parser(description="""Remove sentences with any Latin characters""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def accept_only_amharic_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), contains_latin_characters_wrapper), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
