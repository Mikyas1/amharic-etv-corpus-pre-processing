import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
tokenizer = MT5Tokenizer.from_pretrained("google/mt5-base")
model = MT5ForConditionalGeneration.from_pretrained('google/mt5-base')

def msize(m):
    return sum(p.numel() for p in m.parameters())


print(msize(model.shared) / msize(model))
print(msize(model.lm_head) / msize(model))

am_sentence = "ስላልመጣች ልሂድ አለችጘ።"
print(tokenizer.tokenize(am_sentence))