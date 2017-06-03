from __future__ import division
import nltk,re , pprint
from nltk import word_tokenize

import urllib2
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urllib2.urlopen(url)
raw = response.read().decode('utf8')
print raw[:50]
