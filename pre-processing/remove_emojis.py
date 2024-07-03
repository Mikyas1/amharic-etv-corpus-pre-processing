import re
from utils.helpers import *

def remove_emojis(sentence):
    # Define emoji pattern
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols & Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', sentence).strip()

# Example usage
# sentences = [
#     "Hello 😊, how are you? 🌟",
#     "This is a test sentence with an emoji 👍.",
#     "No emojis here!",
#     "የኮሪደር ልማት ስራዎቻቸው ተጠናቀው ለአገልግሎት 📷"
# ]

# for sentence in sentences:
#     print(f"'{remove_emojis(sentence)}'")


def main():
    args = arg_parser(description="""Removes all emojis from sentences""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_emojis_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), remove_emojis), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
