from utils.helpers import *

def remove_white_spaces(sentence):
    # Regex pattern to match URLs
    return sentence.strip()



def main():
    args = arg_parser(description="""Remove white spaces from all sentences""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_white_space_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), remove_white_spaces), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
