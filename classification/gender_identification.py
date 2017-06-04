import nltk,random
from nltk.corpus import names

#feature function
def gender_feature(word):
    return {'last_letter':word[-1]}

def gender_feature2(word):
    features = {}
    features['first_letter'] = word[0].lower()
    features['last_letter'] = word[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

labeled_names = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)


featuresets = [(gender_feature2(n),gender) for (n,gender) in labeled_names]
test_set = featuresets[:500]
train_set = featuresets[500:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

#accuracy on test_set
print 'Accuracy :'+ str(nltk.classify.accuracy(classifier, test_set))


print classifier.show_most_informative_features(5)
