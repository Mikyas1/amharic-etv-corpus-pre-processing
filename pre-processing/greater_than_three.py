from utils.helpers import *

def has_more_than_three_words(sentence):
    words = sentence.split()  # Split the sentence into words based on whitespace
    return len(words) > 3

def has_more_than_three_words_wrapper(sentence):
    if has_more_than_three_words(sentence=sentence):
        return sentence
    return None

def main():
    args = arg_parser(description="""Remove less than three sentences""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_less_than_three_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), has_more_than_three_words_wrapper), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
