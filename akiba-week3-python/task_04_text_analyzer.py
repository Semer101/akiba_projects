def count_words(sentence):
    punctuation = ",.:;?!"
    for char in punctuation:
        sentence = sentence.replace(char, "")
        
    words = sentence.split()
    return len(words)


def count_chars(sentence):
    count_char = 0
    punctuation = ".,!?:;"
    
    for char in punctuation:
        sentence = sentence.replace(char, "")

    for char in sentence:
            if char != " ":
                count_char += 1

    return count_char


def count_vowels_consonants(sentence):
    sentence = sentence.lower()
    vowel = 0
    consonant = 0
    for i in sentence:
        if i in "aeiou":
            vowel += 1
        elif i in "bcdfghjklmnpqrstvwxyz":
            consonant += 1
        else:
            continue
    return vowel, consonant


def longest_word(sentence):
    punctuation = ".,!?:;"
        
    for char in punctuation:
        sentence = sentence.replace(char, "")

    lst = sentence.split()
  
    if len(lst) > 0:
        longest = lst[0]
        for word in lst:
            if len(word) > len(longest):
                longest = word
        return longest
    else:
        return ""


def word_counter(sentence):
    sentence = sentence.lower()
    punctuation = ".,!?:;"

    for char in punctuation:
        sentence = sentence.replace(char, "")

    lst = sentence.split()
    word_counts = {}

    for word in lst:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def repeated_words(sentence):
    word_counts = word_counter(sentence)
    new_lst = {}
    for key,value in word_counts.items():
        if value > 1:
            new_lst[key] = value
       
    return new_lst


def five_most_frequent(sentence):
    word_counts = word_counter(sentence)

    sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)
    return sorted_words[:5]

def visualize_results(sentence):
    words = count_words(sentence)
    chars_count = count_chars(sentence)
    vowels, consonants = count_vowels_consonants(sentence)
    long_word = longest_word(sentence)
    words_counts = word_counter(sentence)
    repeats = repeated_words(sentence)
    five_frequent = five_most_frequent(sentence)

    print(f"Word: {words}")
    print(f"Characters: {chars_count}")
    print(f"Vowels: {vowels} and consonants: {consonants} ")
    print(f"Longest word: {long_word}")
    print(f"Word counts: {words_counts}")
    print(f"Repeated words: {repeats}")
    print(f"Five most frequent: {five_frequent}")

sentence = "Python is useful and Python is powerful."
visualize_results(sentence)