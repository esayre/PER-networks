from __future__ import print_function
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re

'''-------------------------------------------------------------------------------------------------------'''

# import three lists: titles, links and wikipedia synopses
titles = open('C:\Users\Waika Wong\PycharmProjects\untitled11\score').read().split('\n')

print(str(len(titles)) + ' titles')

synopses_imdb = open('C:\Users\Waika Wong\PycharmProjects\untitled11\Listss').read().split('\n\nBREAKS HERE\n')

synopses_clean_imdb = []
for text in synopses_imdb:
    text = BeautifulSoup(text, 'html.parser').getText()
    #strips html formatting and converts to unicode
    synopses_clean_imdb.append(text)

synopses_imdb = synopses_clean_imdb

synopses = []

for i in range(len(synopses_imdb)):
    item =  synopses_imdb[i]
    synopses.append(item)


# generates index for each item in the corpora (in this case it's just rank) and I'll use this for scoring later
ranks = []

for i in range(0,len(titles)):
    ranks.append(i)

'''---------------------------------------------------------------------------------------------------------'''

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

# here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in synopses:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print ('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')

'''---------------------------------------------------------------------------------------------------------'''

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

"(document id, term number) tfidf score"

tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)

terms = tfidf_vectorizer.get_feature_names()

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)

'''---------------------------------------------------------------------------------------------------------'''

from sklearn.cluster import KMeans

num_clusters = 15

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

from sklearn.externals import joblib

joblib.dump(km,  'doc_cluster.pkl')
km = joblib.load('doc_cluster.pkl')

'''------------------------------------------------------------------------------------------------------------'''

import pandas as pd

films = {'title': titles, 'rank': ranks, 'synopsis': synopses, 'cluster': clusters}

frame = pd.DataFrame(films, index = [clusters] , columns = ['rank', 'title', 'cluster'])

frame['cluster'].value_counts()

grouped = frame['rank'].groupby(frame['cluster'])

grouped.mean()

"""--------------------------------------------------------------------------------------------------------------"""

print("Top terms per cluster:")
print()
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    '''print("Cluster %d words:" % i, end='')
    for ind in order_centroids[i, :6]:
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print()
    print()'''
    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print()
    print()

"""--------------------------------------------------------------------------------------------------------------"""

fp = open("C:\Users\Waika Wong\PycharmProjects\untitled11\Results","wb")

fp.write("Top terms per cluster:")
fp.write("\n")
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    fp.write("Cluster ")
    fp.write(str(i))
    fp.write(" titles: ")
    for title in frame.ix[i]['title'].values.tolist():
        fp.write(str(title))
    fp.write("\n")
    fp.write("\n")

"-------------------------------------------------------------------------------------------------------------------"

