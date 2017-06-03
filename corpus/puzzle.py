import nltk

puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()

a=[w for w in wordlist if len(w)==5 and obligatory in w and nltk.FreqDist(w)<=puzzle_letters]
print len(a)
