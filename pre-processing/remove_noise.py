from utils.helpers import *


def is_source(sentence):
    words = sentence.strip().split()
    if (len(words) <= 3 and words[0].startswith("በ")) or words[0].startswith("ምንጭ"):
        return True
    return False


def corpus_specific_noise(sentence):
    starts_with = ["ጤና ይስጥልኝ ኢትዮጵያ", "የዕለቱ"]
    return any(sentence.startswith(prefix) for prefix in starts_with)


def corpus_noise_transformer(sentence):
    if is_source(sentence) or corpus_specific_noise(sentence):
        return None
    return sentence

def main():
    args = arg_parser(description="""Removes sentence which have corpus specific noise""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_corpus_noise():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), corpus_noise_transformer), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
