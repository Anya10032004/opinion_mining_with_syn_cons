# 1. Specify the training data and output file
import json
train_path =   r"C:\Users\Anya\OneDrive\Documents\GitHub\opinion_mining_with_syn_cons\data\mqpa_in_jsonformat\train.json"
output_path = r"C:\Users\Anya\OneDrive\Documents\GitHub\opinion_mining_with_syn_cons\data\char_vocab_file\opinion0.train.conll12.train.char.txt"
import os
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("File exists:", os.path.exists(train_path))
print("Folder exists:", os.path.exists(os.path.dirname(train_path)))

if os.path.exists(os.path.dirname(train_path)):
    print("Files in folder:")
    print(os.listdir(os.path.dirname(train_path)))

# 2. Collect unique characters
characters = set()

with open(train_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        # # Skip empty lines
        if not line:
            continue

        data = json.loads(line)
        sentences = data["sentences"]

        for word in sentences:
            for char in word:
                characters.add(char)


        # # Split a CoNLL line into columns
        # columns = line.split()

        # Assuming the first column contains the word
        # word = columns[0]

        # for char in word:
        #     characters.add(char)

       

# 3. Sort characters for consistent ordering
characters = sorted(characters)

# 4. Save one character per line
with open(output_path, "w", encoding="utf-8") as file:
    for char in characters:
        file.write(char + "\n")

print(f"Character vocabulary created: {output_path}")
print(f"Total unique characters: {len(characters)}")