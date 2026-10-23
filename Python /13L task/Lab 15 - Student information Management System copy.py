# #plindrome words

# #checking if the word is palindrome or not

# if __name__ == "__main__":
#     word = input("Enter a word: ")
#     if word == word[::-1]:
#         print(f"{word} is a palindrome.")
#     else:
#         print(f"{word} is not a palindrome.")


# text=input().lower().split()

# frequency={}

# for word in text:
#     frequency[word]=frequency.get(word,0)+1

# for word in sorted(frequency):
#     print(f"{word}:{frequency[word]}")

 
# for i in range(1, 6):
#      squares.append(i ** 2)
# print(squares)

squares=(i**2 for i in range(1,6))

print(list(squares))