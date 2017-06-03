import nltk
from nltk.corpus import brown
news_text= brown.words(categories='news')


#stylistic
fdist= nltk.FreqDist(w.lower() for w in news_text)
models=['when','what','why','which','whom','where']
for words in models:
	print words +' : '+ '%d'%(fdist[words])


#cumulative frequency distribution
cfd= nltk.ConditionalFreqDist(
	(genre,word)
	for genre in brown.categories()
	for word in brown.words(categories=genre)
	)

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
