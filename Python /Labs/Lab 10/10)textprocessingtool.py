# Save your file as: lab10_text_processing.py

print("=========================================")
print("         LOVISH'S TEXT PROCESSING TOOL           ")
print("=========================================")

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")
print()

print("=====Processing Results =====")  

# 2. Display a character at a specific position using string indexing
pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos} : '{sentence[pos]}'")

# 3. Extract a portion of the sentence using string slicing
start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
sliced = sentence[start:end]
print(f"Sliced string [{start}:{end}]         : '{sliced}'")

# 4. Convert the sentence into uppercase
print(f"Uppercase                  : {sentence.upper()}")

# 5. Convert the sentence into lowercase
print(f"Lowercase                  : {sentence.lower()}")

# 6. Replace a specified word with another word
word_to_replace = input("Enter word to replace      : ")
replacement_word = input("Enter replacement word     : ")
replaced_sentence = sentence.replace(word_to_replace, replacement_word)
print(f"After replace              : {replaced_sentence}")

# 7. Find and display the length of the sentence
print(f"Length of sentence         : {len(sentence)}")
print()

print("=========================================")
print("Analysis Completed!!!!")
print("=========================================")