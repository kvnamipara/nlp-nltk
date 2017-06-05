import nltk

posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word).lower()] = True
    return features

featuresets = [(dialogue_act_features(post.text),post.get('class')) for post in posts]

size = int(len(featuresets)*0.1)
test_set = featuresets[:size]
train_set = featuresets[size:]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'Accuracy : '+ str(nltk.classify.accuracy(classifier,test_set))
print classifier.show_most_informative_features(5)
