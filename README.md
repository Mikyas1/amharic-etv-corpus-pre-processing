### TO GET TOTAL LINES OF A TEXT FILE

- wc -l <file_name.txt>

### RESOURCES FOR CORPUS CLEANING AND PRE-PROCESSING

- https://aclanthology.org/W18-3809.pdf

### Pre-processing steps

1. remove all sentences with no amharic characters (./pre-processing/extract_with_amh_char.py)

   - python extract_with_amh_char.py ../corpus/EBCNEWSNOW.txt ../corpus/atlist_one_amh_char_per_sentence.txt
     -- reduced initial corpus from 47172946 to 26125564 lines
   - Ex:
     -- Removed None, "", only english sentences, spacers like **\*\*\***, --------

2. remove all URLs from the sentences (./pre-processing/remove_urls.py)

   - python remove_urls.py ../corpus/atlist_one_amh_char_per_sentence.txt ../corpus/url_free.txt
     -- reduced url free corpus from 26125564 to 26125314 lines
   - Ex:
     -- በዚህም መሰረት በፖሊሲው የትግበራ ምዕራፍ የሚከናወኑ ተግባራትን በዝርዝር የያዘ ረቂቅ ፍኖተ ካርታ ተጠናቅቆ ለውይይት ዝግጁ መሆኑን ይፋ አድርጓል።https://www.facebook.com/<> -> በዚህም መሰረት በፖሊሲው የትግበራ ምዕራፍ የሚከናወኑ ተግባራትን በዝርዝር የያዘ ረቂቅ ፍኖተ ካርታ ተጠናቅቆ ለውይይት ዝግጁ መሆኑን ይፋ አድርጓል።

3. remove lists (starting with 1. 2. 3. .... or • ) from sentences

   - python remove_list_indicators.py ../corpus/url_free.txt ../corpus/no_list.txt
     -- reduced corpus from 26125314 to 26125314 lines
   - Ex:
     -- 2. አቶ ቻም ኡቦንግ* የክልሉ ፍትህ ቢሮ ኃላፊ -> አቶ ቻም ኡቦንግ* የክልሉ ፍትህ ቢሮ ኃላፊ
     -- • ከአራት ኪሎ እስከ ቅ/ማሪያም ቤ/ክርስቲያን መታጠፊያ -> ከአራት ኪሎ እስከ ቅ/ማሪያም ቤ/ክርስቲያን መታጠፊያ

4. remove noises sources, short sentences (3 len max) if they start with በ or any sentence starting with ምንጭ, contain corpus specific noise words like ጤና ይስጥልኝ ኢትዮጵያ ....

   - python remove_noise.py ../corpus/no_list.txt ../corpus/less_noise.txt
     -- reduced corpus from 26125314 to 25423016 lines

5. remove quotations in the corpus,

   - python remove_quote.py ../corpus/less_noise.txt ../corpus/less_quote.txt
     -- reduced corpus from 25423016 to 25423016 lines

   - Ex:
     -- የኮሪደር ልማት ስራዎቻቸው ተጠናቀው ለአገልግሎት ክፍት በተደረጉት መንገዶች ላይ ተሽከርካሪዎችን አቁሞ መሄድ ክልክል ነው - አዲስ አበባ ፖሊስ -> የኮሪደር ልማት ስራዎቻቸው ተጠናቀው ለአገልግሎት ክፍት በተደረጉት መንገዶች ላይ ተሽከርካሪዎችን አቁሞ መሄድ ክልክል ነው
     -- የጃፓን ባለሐብቶች በኢንዱስትሪ ፓርኮች ኢንቨስት እንዲያደርጉ እየተሰራ ነው፡ - በኢትዮጵያ የጃፓን አምባሳደር -> የጃፓን ባለሐብቶች በኢንዱስትሪ ፓርኮች ኢንቨስት እንዲያደርጉ እየተሰራ ነው

6. remove spacers like ---------, **\*\*\***, ... and replace them with "\n"

   - python remove_spacers.py ../corpus/less_quote.txt ../corpus/no_spacers.txt
     -- increased corpus from 25423016 to 25460539 lines

7. remove spacer like " "\*4, more than one with " " (replace multiple spaces with single space)

   - python remove_multiple_spaces.py ../corpus/no_spacers.txt ../corpus/no_multiple_spacers.txt
     -- increased corpus from 25460539 to 25460539 lines

8. emoji removal

   - python remove_emojis.py ../corpus/no_multiple_spacers.txt ../corpus/no_emojis.txt
     -- increased corpus from 25460539 to 25460539 lines

9. separate paragraphs in to sentences

   - python split_paragraph.py ../corpus/no_emojis.txt ../corpus/no_paragraphs.txt
     -- increased corpus from 25460539 to 26494127 lines

10. strip all white spaces of sentences

    - python strip_sentences.py ../corpus/no_paragraphs.txt ../corpus/no_white_spaces.txt
      -- increased corpus from 26494127 to 26494127 lines

11. all sentences must contain at list 3 words

    - python greater_than_three.py ../corpus/no_white_spaces.txt ../corpus/greater_than_three.txt
      -- reduced corpus from 26494127 to 25827969 lines

12. all sentences must be amharic latter or punctuation marks

    - python only_amharic.py ../corpus/greater_than_three.txt ../corpus/only_amharic.txt
      -- reduced corpus from 25827969 to 25542208 lines

13. all sentences must be unique implement binary search with hashing to speed up this process

    - python unique_sentences.py ../corpus/only_amharic.txt ../corpus/clean_dataset.txt
      -- reduced corpus from 25827969 to 99302 lines
