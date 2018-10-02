from abstracts import Abs1
from dict import stopwords
from numpy import zeros
import string

wordlist_without_stopwords = []
wordfreq = []
wordlist_with_stopwords = []
wordlist_with_stemmed_words = []

#Functions

def removeStopwords(wordlist, stopwords):
    return(w for w in wordlist if w not in stopwords)

def count_elements(lst):
    elements={}
    for elem in lst:
        if elem in elements.keys():
            elements[elem]+=1
        else:
            elements[elem]= 1
    return elements

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's','al']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def output_dictionary_values(my_dict):
    for key, value in my_dict.items():
        return(value)

#Main Module

asking = ''.join([c for c in Abs1 if c not in ('!', '?',"'",":","'",";",",",".","@","(",")","-","-")]) #Removing punctuaction

wordlist = asking.split() #Splitting all words of the document

text_without_stopwords = removeStopwords(wordlist,stopwords) #Remove all stop words

for w in text_without_stopwords: #Appehend all significant words inside the matrix: wordlist_without_stopwords
    if w not in stopwords:
        wordlist_without_stopwords.append(w)
    continue

for w in wordlist_without_stopwords: #Stem all words in the matrix wordlist_without_stopwords and appehend
    B = stem(w)                      #in a new matrix wordlist_with_stemmed_words
    wordlist_with_stemmed_words.append(B)

v1 = count_elements(wordlist_with_stemmed_words)

J = output_dictionary_values(v1)

#print("String\n" + wordstring +"\n")
#print("List without Stopwords and steemed\n" + str(wordlist_with_stemmed_words) + "\n")
#print("Frequencies\n" + str(count_elements(wordlist_with_stemmed_words)) + "\n")


