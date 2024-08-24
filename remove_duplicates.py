import sys
import pandas as pd

TEMP = sys.argv[1] # 1.0 or 1.1 or 1.2 (higher for more creativity, but less coherence)

# read data from generated_sequences.txt
with open(f"generated_sequences_temp_{TEMP}.txt", "r") as f:
    gpt = f.readlines()

omic = pd.read_csv("data/unique_Omicron_2k.csv")["sequence"].to_list()
new = pd.read_csv("data/unique_New_2k.csv")["sequence"].to_list()
eris = pd.read_csv("data/unique_Eris_2k.csv")["sequence"].to_list()

targets = [gpt, omic, new, eris]
target_names = ["Gpt", "Omicron", "New", "Eris"]

def get_unique(gpt, targets, target_names):
    unique_sequences = {}
    for target, target_name in zip(targets, target_names):
        # count duplicates with target
        duplicates = 0
        for i in range(len(gpt)):
            for j in range(i+1, len(target)):
                unique_sequences[gpt[i]] = 1
                if gpt[i] == target[j]:
                    duplicates += 1
        print(f"Number of duplicates with {target_name}: {duplicates}")
    return unique_sequences

unique_sequences = get_unique(gpt, targets, target_names)

# write data to file
counter = 0
with open(f"unique_generated_sequences_temp_{TEMP}.txt", "w") as f:
    for seq in unique_sequences:
        f.write(seq)
        counter += 1

print(f"Number of unique sequences written to file: {counter}")