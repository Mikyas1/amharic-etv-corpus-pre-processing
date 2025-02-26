import multiprocessing
from utils.helpers import *

import random
import re
import string
import hm


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

def process_amharic_sentence(amharic_input_sentence):
    print("done on line")
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
                return f"{result} ---->>> updated ---->>> {amharic_input_sentence}"

        elif current_pos == "V" and next_pos == "V":
            if random.random() < 0.5:
                swap_words(words, i, i + 1)
                result = ' '.join(words)
                return f"{result} ---->>> updated  ---->>> {amharic_input_sentence}"

        else:
            if random.random() < 0.1:
                swap_words(words, i, i + 1)
                result = ' '.join(words)
                return f"{result} ---->>> updated  ---->>> {amharic_input_sentence}"

    return amharic_input_sentence + " ---->>> No-updated  ---->>> ?????"


def read_lines(file_name, output_file, start_line, threads, write_lock):
    with open(output_file, 'a') as outfile:        
  
      i = 1
      for line in read_file_and_yield_line(file_name):
          if ((i - start_line) % threads) == 0:
                #   with write_lock:
                  # print(line, i, start_line)
                write_lock.acquire()
                try:
                    outfile.write(f'{process_amharic_sentence(line)}\n')
                finally:
                    write_lock.release()
          i += 1
    


      


def main():
    args = arg_parser(description="""Wordorder error generation with multithreading""", 
                              input_dict=standard_input_output_args,)
    
    file_name = args.input_file
    output_file = args.output_file
    
    lock = multiprocessing.Lock()
    
    # Create three process for reading lines with different starting points
    process1 = multiprocessing.Process(target=read_lines, args=(file_name, output_file, 1, 4, lock))
    process2 = multiprocessing.Process(target=read_lines, args=(file_name, output_file, 2, 4, lock))
    process3 = multiprocessing.Process(target=read_lines, args=(file_name, output_file, 3, 4, lock))
    process4 = multiprocessing.Process(target=read_lines, args=(file_name, output_file, 4, 4, lock))

    # Start the threads
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    # process5.start()
    # process6.start()

    # Wait for all processs to complete
    process1.join()
    process2.join()
    process3.join()
    process4.join()


if __name__ == "__main__":
    main()