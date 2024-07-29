import random
import re
from utils.helpers import *
import string
import hm

import csv

# load language
# hm.download('a')

def remove_last_punctuation(sentence):
    # Define the punctuation marks you want to remove
    punctuation_marks = {'?', '።', '!'}
    
    # Check if the last character is a punctuation mark
    if sentence and sentence[-1] in punctuation_marks:
        return sentence[:-1], sentence[-1]
    return sentence, ""

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

def get_pos(word):
    _word = remove_punctuation_from_words(remove_punctuation_from_words_amh(word))
    w1 = hm.anal('a', _word)
    return w1[0]['pos']

def swap_words(sentence, index1, index2):
    # Helper function to swap two words in a list
    sentence[index1], sentence[index2] = sentence[index2], sentence[index1]

def process_amharic_sentence(input):
    print("done on line")
    amharic_input_sentence, last_punctuation = remove_last_punctuation(input)
    words = amharic_input_sentence.split()
    num_words = len(words)
    
    for i in range(num_words - 1):
        current_word = words[i]
        next_word = words[i + 1]
        current_pos = get_pos(current_word)
        next_pos = get_pos(next_word)
        
        if current_pos == "N" and next_pos == "V":
            if random.random() < 0.5:
                swap_words(words, i, i + 1)
                result = ' '.join(words)
                # return f"{result + last_punctuation} ---->>> updated ---->>> {input} ---->>> index {i} with {i + 1}"
                return [f"{result + last_punctuation}", input, "wo", "t", i, i+1, current_word, num_words]

        elif current_pos == "V" and next_pos == "V":
            if random.random() < 0.5:
                swap_words(words, i, i + 1)
                result = ' '.join(words)
                # return f"{result + last_punctuation} ---->>> updated  ---->>> {input} ---->>> index {i} with {i + 1}"
                return [f"{result + last_punctuation}", input, "wo", "t", i, i+1, current_word, num_words]

        else:
            if random.random() < 0.1:
                swap_words(words, i, i + 1)
                result = ' '.join(words)
                # return f"{result + last_punctuation} ---->>> updated  ---->>> {input} ---->>> index {i} with {i + 1}"
                return [f"{result + last_punctuation}", input, "wo", "t", i, i+1, current_word, num_words]

    # return input + " ---->>> No-updated  ---->>> ?????"
    return [input, input, "wo", "f", "", "", "", ""]


def main():
    args = arg_parser(description="""Wordorder error generation""", 
                              input_dict=standard_input_output_args,)
    
    
    headers = ['incorrect', 'correct', 'error_type', 'error_exists', 'first_index', 'second_index', 'first_word', 'second_word']
    @with_info
    def wordorder_error_generation():
        write_lines_to_csv_file(headers=headers)(transformer(read_file_and_yield_line(args.input_file), process_amharic_sentence), args.output_file) 
 
if __name__ == "__main__":
    main()
