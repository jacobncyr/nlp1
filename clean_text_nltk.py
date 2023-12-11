import nltk
#import and download tools
# nltk.download()
filename = 'metamorph.txt'
file = open(filename,"rt",encoding="utf-8")
text = file.read()
file.close()

#split into sentances
# from nltk import sent_tokenize
#
# sentences = sent_tokenize(text)
# print(sentences[1])

#split into words with tokenize
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])

words = [word for word in tokens if word.isalpha()]
print(words[:100])


from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]

print(stemmed[:100])