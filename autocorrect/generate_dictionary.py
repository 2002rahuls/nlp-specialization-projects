import nltk
nltk.download('words')
from nltk.corpus import words

word_list = words.words()

with open("dictionary.txt", "w") as file:
    for word in word_list:
        file.write(f"{word.lower()}\n")
