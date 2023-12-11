# load text data into memory
import string

filename = 'metamorph.txt'
file = open(filename,'rt', encoding='utf-8')
text = file.read()
file.close()

#3 ways to clean your data

#split into tokens, tokens are words
# words = text.split()
# print(words[:100])

#use regex to select the words
# import re
# words = re.split(r'\W+',text)
# print(words[:100])

#split by whitespace and remove punctuation
# words = text.split()
# print(string.punctuation)
# table = str.maketrans("","",string.punctuation)
# stripped = [w.translate(table) for w in words]
# print(stripped[:100])

#normalize the case for all words to remove redundancies
words = text.split()
words = [word.lower() for word in words]
print(words[:100])