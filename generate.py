from transformers import pipeline
import time

protgpt2 = pipeline('text-generation', model="./output_1e-3", device=0)

# length is expressed in tokens, where each token has an average length of 4 amino acids.
begin = time.time()
seq_dict = protgpt2("<|endoftext|>MFVF", min_length=300, max_length=500, do_sample=True, top_k=950, repetition_penalty=1.2, num_return_sequences=10, eos_token_id=0)
end = time.time()

# Elapsed time in hh:mm:ss format
elapsed = end - begin
print("Elapsed time: " + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

# Write generated sequences to a file
with open("generated_sequences.txt", "w") as f:
    for item in seq_dict:
            raw_seq = item['generated_text']
            clean_seq = raw_seq.replace("<|endoftext|>", "").replace("\n", "")
            if len(clean_seq) > 1235 and len(clean_seq) < 1280:
                # print(clean_seq)
                f.write(clean_seq + "\n")