
import torch
import math
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import time

def calculatePerplexity(sequence, model, tokenizer, device):
    input_ids = torch.tensor(tokenizer.encode(sequence)).unsqueeze(0) 
    input_ids = input_ids.to(device)
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss, _ = outputs[:2]
    return math.exp(loss)


model = GPT2LMHeadModel.from_pretrained('./output_1e-3')
tokenizer = GPT2Tokenizer.from_pretrained('./output_1e-3')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# read sequences from txt file
sequences = []
with open("generated_sequences.txt", "r") as f:
    for line in f:
        seq = line.strip()
        # add "<|endoftext|>" to the beginning of each sequence
        seq = "<|endoftext|>" + seq
        sequences.append(seq)


# calculate perplexity for each sequence
begin = time.time()

perplexities = []
for seq in sequences:
    ppl = calculatePerplexity(seq, model, tokenizer, device)
    print(ppl)
    perplexities.append(ppl)

end = time.time()
elapsed = end - begin
print("Elapsed time: " + time.strftime('%H:%M:%S', time.gmtime(elapsed)))


# write perplexities to a file
with open("generated_ppls.txt", "w") as f:
    for p in perplexities:
        f.write(str(p) + "\n")