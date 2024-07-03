# from transformers import T5ForConditionalGeneration, T5Tokenizer
# model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
# tokenizer = T5Tokenizer.from_pretrained('t5-small')

# sentence = "I like to swimming"
# tokenized_sentence = tokenizer('gec: ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
# corrected_sentence = tokenizer.decode(
#     model.generate(
#         input_ids = tokenized_sentence.input_ids,
#         attention_mask = tokenized_sentence.attention_mask, 
#         max_length=128,
#         num_beams=5,
#         early_stopping=True,
#     )[0],
#     skip_special_tokens=True, 
#     clean_up_tokenization_spaces=True
# )
# print(corrected_sentence)

from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
# model = T5ForConditionalGeneration.from_pretrained("google/mt5-small")
tokenizer = T5Tokenizer.from_pretrained('google/mt5-small')

# sentence = "I like to swimming"
am_sentence = "የፒያሳ እና የአራት ኪሎ መስመር ስራ በተያዘው የሦስት ወር መርሐ-ግብር ማጠናቀቃችንን ስገልፅ ደስታ ይሰማኛል፦ ጠቅላይ ሚኒስትር ዐቢይ አሕመድ (ዶ/ር)"
# tokenized_sentence = tokenizer('translate Amharic to English: : ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
print(tokenizer.tokenize(am_sentence))

# tokenized_sentence = tokenizer('gec: ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')

# corrected_sentence = tokenizer.decode(
#     model.generate(
#         input_ids = tokenized_sentence.input_ids,
#         attention_mask = tokenized_sentence.attention_mask, 
#         max_length=128,
#         num_beams=5,
#         early_stopping=True,
#     )[0],
#     skip_special_tokens=True, 
#     clean_up_tokenization_spaces=True
# )
# print(corrected_sentence)