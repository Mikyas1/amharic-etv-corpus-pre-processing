import re
from utils.helpers import *

def remove_url(sentence):
    # Regex pattern to match URLs
    url_pattern = r'http[s]?://\S+'
    # Replace URLs with an empty string
    cleaned_text = re.sub(url_pattern, '', sentence)
    return cleaned_text.strip()



def main():
    args = arg_parser(description="""Removes URL from sentences for every line
                              in the given input file and saves it to out put file""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_url_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), remove_url), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
