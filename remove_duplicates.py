# read data from generated_sequences.txt
with open("generated_sequences.txt", "r") as f:
    data = f.readlines()

# count duplicates
duplicates = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] == data[j]:
            duplicates += 1

print(f"Number of duplicates: {duplicates}")

# remove duplicates
data = list(set(data))

# write data to file
with open("unique_generated_sequences.txt", "w") as f:
    for item in data:
        f.write(item)