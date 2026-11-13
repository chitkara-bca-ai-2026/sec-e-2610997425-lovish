#  TAKE INPUT FROM THE USER
Sentence = input("Enter a sentence: ")

# Intialize counter:-
words = len(Sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

vowel_set = "aeiouAEIOU"

#  Analyse the sentence:-
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

# CALCULATE VOWEL PERCENTAGE:-
vowel_percentage = (vowels / total_letters) * 100 if total_letters > 0 else 0

#  DISPLAY THE RESULTS:-
print("=" * 45)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 45)
print(f"Sentence: {Sentence}")
print(f"Total characters: {total_characters}\n")

print("====CHARACTER BREAKDOWN====")
print(f"WORDS:              {words}")
print(f"VOWELS:             {vowels}")
print(f"CONSONANTS:         {consonants}")
print(f"DIGITS:             {digits}")
print(f"SPACES:             {spaces}")
print(f"SPECIAL CHARACTERS: {special_characters}\n")

print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print("=" * 45)
print("ANALYSIS COMPLETED FINALLY!!!")
print("=" * 45)