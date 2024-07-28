from utils.helpers import *
import hm
import string

import re

def remove_punctuation_from_words_amh(text):
    # Regular expression pattern to match words and attached punctuation
    pattern = r'\b\w+[\.,;:\-!?\u2018\u2019\u201C\u201D]*|\b[\.,;:\-!?\u2018\u2019\u201C\u201D]+'
    
    # Find all matches using the regular expression pattern
    matches = re.findall(pattern, text)
    
    # Filter out punctuation and keep only words
    words = [match for match in matches if not re.match(r'^[\.,;:\-!?\u2018\u2019\u201C\u201D]+$', match)]
    
    # Join the words back into a single string with spaces between them
    result = ' '.join(words)
    
    return result

def remove_punctuation_from_words(text):
    # Define a pattern to match any punctuation character
    punctuation_pattern = f"[{re.escape(string.punctuation)}]"
    
    # Replace all punctuation characters with an empty string
    cleaned_text = re.sub(punctuation_pattern, '', text)
    
    # Remove any extra spaces that might result from punctuation removal
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

def pos_print(sentence):
  for word in sentence.split():
    _word = remove_punctuation_from_words(remove_punctuation_from_words_amh(word))
    w1 = hm.anal('a', _word)
    result = f"{_word}, {w1[0]['pos']}"
    print(result) 
    yield result

def main():
    args = arg_parser(description="""Word pos""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def only_unique_sentences():
        write_lines_to_file(transformer_to_multi_lines(read_file_and_yield_line(args.input_file), pos_print), args.output_file)

if __name__ == "__main__":
    main()
