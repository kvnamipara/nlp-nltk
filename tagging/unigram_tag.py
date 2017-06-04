import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

#tag 20th sentence
print unigram_tagger.tag(brown_sents[20])
#print accuracy with given tagged sentence
print unigram_tagger.evaluate(brown_tagged_sents)
