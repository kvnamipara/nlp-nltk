import nltk
from nltk.corpus import brown
news_text= brown.words(categories='news')
fdist= nltk.FreqDist(w.lower() for w in news_text)

models=['when','what','why','which','whom','where']
for words in models:
	print words +' : '+ '%d'%(fdist[words])

