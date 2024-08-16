from transformers import pipeline
import time

protgpt2 = pipeline('text-generation', model="./output_1e-3", device=0)

prefix0 = "MF" # 1979 out of 2000 starts with this prefix
prefix1 = "MFVFLVLLPLVSSQCVNL" # 1878 out of 2000 starts with this prefix
prefix2 = "MFVFLVLLPLVSSQCVNLITRTQ" # 1528 out of 2000 starts with this prefix

# length is expressed in tokens, where each token has an average length of 4 amino acids.
begin = time.time()
seq_dict = protgpt2(f"<|endoftext|>{prefix1}", min_length=300, max_length=500, do_sample=True, top_k=950, repetition_penalty=1.2, num_return_sequences=100, eos_token_id=0)
end = time.time()

# Elapsed time in hh:mm:ss format
elapsed = end - begin
print("Elapsed time: " + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

# Write generated sequences to a file
counter = 0
with open("generated_sequences.txt", "a") as f:
    for item in seq_dict:
            raw_seq = item['generated_text']
            clean_seq = raw_seq.replace("<|endoftext|>", "").replace("\n", "")
            if len(clean_seq) > 1235 and len(clean_seq) < 1280:
                counter += 1
                f.write(clean_seq + "\n")

print(f"Number of sequences written to file: {counter}")