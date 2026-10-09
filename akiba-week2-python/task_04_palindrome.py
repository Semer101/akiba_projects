word = input("Enter a word: ")
word = word.lower()

reverse_word = ""
for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]

if word == reverse_word:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")
