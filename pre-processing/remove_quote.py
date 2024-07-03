import re
from utils.helpers import *

def remove_quotes(sentence):
    parts = re.split(r'፡ -|፦|:-|፡-| - ', sentence)
    largest_part = max(parts, key=lambda part: len(part.split()))
    return largest_part.strip()


# sentences = [
#     "መንገዶች ላይ ተሽከርካሪዎችን አቁሞ መሄድ ክልክል ነው - አዲስ አበባ ፖሊስ",
#     '"የኢቢሲ ስጦታ ለ60 ዓመታት 6 ሺህ መጻሕፍት"፡- አንጋፋነትን የሚመጥን ማኅበራዊ ኃላፊነት',
#     "በአደጋው አብረዋቸው 8 ሰዎች እንደነበሩ የተገለጸ ሲሆን፤ ጉዟቸው የሀገሪቱን የቀድሞ ጠቅላይ አቃቤ ሕግ የቀብር ሥነ-ሥርዓት ለመካፈል ነበር፡፡"
# ]

# for sentence in sentences:
#     print(remove_quotes(sentence))
        ## መንገዶች ላይ ተሽከርካሪዎችን አቁሞ መሄድ ክልክል ነው
        ## "የኢቢሲ ስጦታ ለ60 ዓመታት 6 ሺህ መጻሕፍት"
        ## በአደጋው አብረዋቸው 8 ሰዎች እንደነበሩ የተገለጸ ሲሆን፤ ጉዟቸው የሀገሪቱን የቀድሞ ጠቅላይ አቃቤ ሕግ የቀብር ሥነ-ሥርዓት ለመካፈል ነበር፡፡

def main():
    args = arg_parser(description="""Removes the quoted that are separated by unique patterns like ፡ - | ፦ | :-| - 
                      from the sentence""", 
                              input_dict=standard_input_output_args,)
    
    @with_info
    def remove_quotes_from_sentences():
        write_lines_to_file(transformer(read_file_and_yield_line(args.input_file), remove_quotes), args.output_file)
     
       
 
if __name__ == "__main__":
    main()
