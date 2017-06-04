import nltk
from nltk import word_tokenize

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""


tokens = word_tokenize(raw)

wnl = nltk.WordNetLemmatizer()
print [wnl.lemmatize(t) for t in tokens]
