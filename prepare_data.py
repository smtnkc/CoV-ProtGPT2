import os
import pandas as pd
import random
random.seed(42)
names = ["Omicron", "New", "Eris"]

# 1) Add <|endoftext|> at the begging of each sequence 
# 2) Add a new line after each 60 characters (I ignored this part, it works better without it)

for name in names:
    print(f"Processing {name}...")
    sequences = pd.read_csv(f'data/unique_{name}_2k.csv')["sequence"].to_list()
    # shuffle sequences
    random.shuffle(sequences)
    # split sequences into train and validation 90/10
    training = sequences[:int(len(sequences)*0.9)]
    validation = sequences[int(len(sequences)*0.9):]
    with open(f'data/unique_{name}_2k_training.txt', 'w') as f:
        for i, seq in enumerate(training):
            # seq = "\n".join([seq[i:i+60] for i in range(0, len(seq), 60)])
            seq = "<|endoftext|>\n" + seq
            f.write(f'{seq}\n')
    with open(f'data/unique_{name}_2k_validation.txt', 'w') as f:
        for i, seq in enumerate(validation):
            # seq = "\n".join([seq[i:i+60] for i in range(0, len(seq), 60)])
            seq = "<|endoftext|>\n" + seq
            f.write(f'<|endoftext|>\n{seq}\n')