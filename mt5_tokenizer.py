from transformers import T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained('google/mt5-small')

sentence = "ከቀይ ባህር ኮንዶሚኒየም በደጎል አደባባይ እስከ ቅ/ጊዮርጊስ ቤ/ክርስቲያን አቅጣጫ ያሉት መንገዶች በትናንትናው ዕለት ተከፍተው አገልግሎት መስጠት መጀመራቸው ይታወቃል።"
english_sentence = "english is a common language, used all over the world"
tokenized_sentence = tokenizer(sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')

print(tokenizer.tokenize(sentence))
# print(tokenized_sentence.input_ids)

print(tokenizer.tokenize(english_sentence))
# print(tokenized_sentence.input_ids)