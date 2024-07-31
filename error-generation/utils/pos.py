import os
import re
import string
import hm
import csv
from .helpers import read_lines_from_csv_file

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


class POS:
    
    def __init__(self, pos_dict_file) -> None:
        self.pos_dict_file = pos_dict_file
        self.pos_in_memory_dict = {}
        self.pos_file_writer = None
        
        file_exists = os.path.isfile(self.pos_dict_file)
        if file_exists:
            loaded_total = 0
            for row in read_lines_from_csv_file(file_path=self.pos_dict_file):
                if len(row) == 2:
                    key, value = row
                    self.pos_in_memory_dict[key] = value
                    loaded_total += 1
            
            print(f"--> loaded POS from file, total {loaded_total}")
                    
                    
        try:
            self.pos_file_writer = open(self.pos_dict_file, mode='a', newline='')
        except Exception as e:
            print(f"An error occurred when opening pos_dict_file for Update: {e}")
        
                    
    def write_pos_to_csv(self, row):
        if self.pos_file_writer is None:
            raise Exception("No pos file writer found")
            
        try:
            writer = csv.writer(self.pos_file_writer)
            if row is not None:
                writer.writerow(row)
                # print("!!!!! able to save to cache")
        except Exception as e:
            print(f"An error occurred: {e}")
    

    def clean(self):
        if self.pos_file_writer is not None:
            self.pos_file_writer.flush()
            self.pos_file_writer.close()
            self.pos_file_writer = None
 
        
    def get_pos(self, word):
        _word = remove_punctuation_from_words(remove_punctuation_from_words_amh(word))
        
        if _word in self.pos_in_memory_dict:
            # print("      loaded from cache -->>")
            return self.pos_in_memory_dict.get(_word, "UNK")
        
        w1 = hm.anal('a', _word)
        word_pos = w1[0]['pos']
        
        self.pos_in_memory_dict[_word] = word_pos
        self.write_pos_to_csv([_word, word_pos])
        return word_pos
    
    # may not work always, use clean manually 
    # def __del__(self):
    #     object.__del__(self)
    #     self.clean()
