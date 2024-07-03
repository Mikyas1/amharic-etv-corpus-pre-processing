from utils.helpers import *
import hashlib

unique_sentences = {}


def hash_sentence(sentence):
    # Encode the sentence to a byte representation
    sentence_bytes = sentence.encode('utf-8')
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the byte-encoded sentence
    hash_object.update(sentence_bytes)
    
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    
    return hash_hex


def sentence_is_duplicate(sentence):
    global unique_sentences
    return unique_sentences.get(hash_sentence(sentence=sentence), None)
        


def unique_sentence_wrapper(sentence):
    global unique_sentences
    existent_sentence = sentence_is_duplicate(sentence=sentence)
    if existent_sentence:
        return None
    sentence_hash = hash_sentence(sentence=sentence)
    unique_sentences[sentence_hash] = sentence
    return sentence



def main():
    args = arg_parser(description="""Remove duplicate sentences form the corpus""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def only_unique_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), unique_sentence_wrapper), args.output_file) 
 
if __name__ == "__main__":
    main()
