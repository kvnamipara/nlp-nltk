import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents)*0.9)
train_sets = brown_tagged_sents[:size]
test_sets = brown_tagged_sents[size:]

bigram_tagger = nltk.BigramTagger(train_sets)

print bigram_tagger.evaluate(test_sets)
