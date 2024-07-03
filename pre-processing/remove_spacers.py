import re
from utils.helpers import *

def remove_spacers_and_return_multiple_lines(sentence):
    # Split on multiple occurrences of dashes, asterisks, or periods
    parts = re.split(r'[-*\.]{2,}', sentence)
    for part in parts:
        yield part.strip()


# Example usage
# sentences = [
#     "ከቴዎድሮስ አደባባይ እስከ -- ማህሙድ ሙዚቃ ቤት  እንዲሁም",
#     "አቶ ቱት ጆክ_ የክልሉ ገቢዎች....  ቢሮ ኃላፊ",
#     "ሙዚቃ ቤት ***** እንዲሁም",
#     "ሙዚቃ ቤት      እንዲሁም",
# ]

# for sentence in sentences:
#     results = split_on_spacers(sentence)
#     for result in results:
#         print(result)


def main():
    args = arg_parser(description="""Removes spacers like ---------, *******, ... and replace them with 
                                    multiple sentences.""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_spacers_sentences():
        write_lines_to_file(transformer_to_multi_lines(
            read_file_and_yield_line(args.input_file), 
            remove_spacers_and_return_multiple_lines), 
                            args.output_file)
     
       
 
if __name__ == "__main__":
    main()
