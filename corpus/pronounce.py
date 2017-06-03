import nltk

entries = nltk.corpus.cmudict.entries()
print len(entries)

#pronounceation dictionalry
for entry in entries[:5]:
    print entry


#find word with some pronounceation
for word,pron in entries:
    if len(pron)==3:
        ph1,ph2,ph3= pron
        if ph1 == 'P' and ph3 == 'T':
            print word, ph2


# word having pronounceation ending like 'nicks'
syllable = ['N', 'IH0', 'K', 'S']
print [word for word,pron in entries if pron[-4:]==syllable]

#word woth pronounceation ending with 'M' and word ending with 'n'
print [word for word,pron in entries if word[-1:]=='n' and pron[-1]=='M']
