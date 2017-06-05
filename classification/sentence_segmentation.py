import nltk

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundries.add(offset-1)

def punct_features(tokens,i):
    return {
    'next-word-capitalized' : tokens[i+1].isupper(),
    'prev-word' : tokens[i-1].lower(),
    'punct' : tokens[i],
    'prev-word-is-one-char' : len(tokens[i-1]) == 1
    }

featuresets = [(punct_features(tokens,i),(i in boundries)) for i in range(1,len(tokens)-1) if tokens[i] in '.?!']

size = int(len(featuresets)*0.1)
test_set , train_set = featuresets[:size],featuresets[size:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print 'Accuracy : ' + str(nltk.classify.accuracy(classifier, test_set))
