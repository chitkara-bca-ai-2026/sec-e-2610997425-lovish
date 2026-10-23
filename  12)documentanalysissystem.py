# 1. Take input from the user
Sentence = input("Enter a sentence: ")

# Intialize counters
words = len(Sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

vowel_set = "aeiouAEIOU"

# 2. Analyse the sentence
for char in Sentence:
    if char in vowel_set:
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_characters += 1
total_characters = len(Sentence)
total_letters = vowels + consonants

# 3.Calculate vowel percentage 
vowel_percentage = (vowels / total_letters) * 100 if total_letters > 0 else 0

# 3. Display the results
print("=" * 45)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 45)
print(f"Sentence: {Sentence}")
print(f"Total characters: {total_characters}\n")

print("--- Character Breakdown ---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special_characters}\n")

print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print("=" * 45)
print("Analysis Complete!")
print("=" * 45)