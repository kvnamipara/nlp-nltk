import nltk
from nltk.corpus import wordnet as wn

a= wn.synsets('motorcar')
#print wn.synset('car.n.01').lemma_names()
#print wn.synset('car.n.01').definition()
#print wn.synset('car.n.01').examples()


#hyponyms
#motorcar = wn.synset('car.n.01')
#types_of_motorcar = motorcar.hyponyms()
#print sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())

#parts made up of
print wn.synset('tree.n.01').part_meronyms()

#substance_meronyms
print wn.synset('tree.n.01').substance_meronyms()

#upper level
print wn.synset('tree.n.01').member_holonyms()
