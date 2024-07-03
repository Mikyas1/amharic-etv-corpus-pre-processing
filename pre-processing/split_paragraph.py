import re
from utils.helpers import *

def replace_colon_at_end(sentence):
    return re.sub(r'[:፡፡፡:]+$', '።', sentence.strip())

def ends_with_punctuation(sentence):
    last_char = sentence.strip()[-1]  # Get the last character of the stripped sentence
    return last_char in ['?', '!', '።', '፡', ':']
     
def split_amharic_paragraph(paragraph):
    # Split on sentence delimiters, excluding single "፡"
    sentences = re.split(r'([።?!]|፡፡|::)', paragraph)
    combined_sentences = [''.join(x).strip() for x in zip(sentences[0::2], sentences[1::2]) if ''.join(x).strip()]

    # Handle the case where the number of parts is odd
    if len(sentences) % 2 != 0:
        last_sentence = sentences[-1].strip()
        if last_sentence:
            combined_sentences.append(last_sentence)
        
    for sentence in combined_sentences:
        sentence_with_proper_ending = replace_colon_at_end(sentence)
        if sentence_with_proper_ending and not ends_with_punctuation(sentence_with_proper_ending):
            yield sentence_with_proper_ending + "።"
        elif sentence_with_proper_ending:
            yield sentence_with_proper_ending

# # Example usage
# paragraph = "የኢትዮጵያ ብሮድካስቲንግ! ኮርፖሬሽን “የዕውቀት፣ የጥበብ:: ሰረት በፖሊሲው የትግበራ? ምዕራፍ የሚከናወኑ "
# result = split_amharic_paragraph(paragraph)

# for sentence in result:
#     print(f"'{sentence}'")

def main():
    args = arg_parser(description="""Split sentences from paragraphs using ። ? ! ፡፡ delimiters""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def split_amharic_paragraph_from_inputs():
        write_lines_to_file(transformer_to_multi_lines(
            read_file_and_yield_line(args.input_file), 
            split_amharic_paragraph), 
                            args.output_file)
     
       
 
if __name__ == "__main__":
    main()