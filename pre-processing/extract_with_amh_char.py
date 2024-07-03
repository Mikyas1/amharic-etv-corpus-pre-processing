import re
import argparse
from utils.helpers import *

def contains_amharic(sentence):
    """
    Checks if a sentence contains at least one Amharic character.
    
    Parameters:
    sentence (str): The sentence to check.
    
    Returns:
    bool: True if the sentence contains at least one Amharic character, False otherwise.
    """
    # Amharic characters Unicode range: \u1200 to \u137F
    amharic_pattern = re.compile(r'[\u1200-\u137F]')
    return bool(amharic_pattern.search(sentence))

def contains_amharic_transformer(sentence):
    if contains_amharic(sentence):
        return sentence
    return None

def main():
    args = arg_parser(description='''
                                     From a given input file corpus, read lines of sentences and
                                     save sentences that have at list one Amharic character
                                     to an output file.
                                     ''', 
                            input_dict=standard_input_output_args,)
    
    write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), contains_amharic_transformer), args.output_file)
    

if __name__ == "__main__":
    main()
