import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents)*0.9)
train_sets = brown_tagged_sents[:size]
test_sets = brown_tagged_sents[size:]


t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sets,backoff=t0)
t2 = nltk.BigramTagger(train_sets,backoff=t1)
print 'test evaluation using Bigram: '+t2.evaluate(test_sets)
t3 = nttk.TrigramTagger(train_sets,backoff=t2)
print 'test evaluation using Trigram: '+ t3.evaluate(test_sets)
