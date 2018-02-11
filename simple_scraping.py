import requests
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def plot_word_freq(url):
     # Make the request and check object type
     r = requests.get(url)
     # Extract HTML from Response object and print
     html = r.text
     # Create a BeautifulSoup object from the HTML
     soup = BeautifulSoup(html, "html5lib")
     # Get the text out of the soup and print it
     text = soup.get_text()
     # Create tokenizer
     tokenizer = RegexpTokenizer('\w+')
     # Create tokens
     tokens = tokenizer.tokenize(text)
     # Initialize new list
     words = []
     # Loop through list tokens and make lower case
     for word in tokens:
         words.append(word.lower())
     # Get English stopwords and print some of them
     sw = nltk.corpus.stopwords.words('english')
     # Initialize new list
     words_ns = []
     # Add to words_ns all words that are in words but not in sw
     for word in words:
         if word not in sw:
             words_ns.append(word)
     # Create freq dist and plot
     freqdist1 = nltk.FreqDist(words_ns)
     freqdist1.plot(25)

def plot_word_freq_file(file):
    f = open(file, 'r')
    text = f.read()
    text = unicode(text, 'utf-8')
    tokenizer = RegexpTokenizer('\w+')
    # Create tokens
    tokens = tokenizer.tokenize(text)
     # Initialize new list
    words = []
     # Loop through list tokens and make lower case
    for word in tokens:
        words.append(word.lower())
     # Get English stopwords and print some of them
    sw = nltk.corpus.stopwords.words('english')
     # Initialize new list
    words_ns = []
     # Add to words_ns all words that are in words but not in sw
    for word in words:
        if word not in sw:
            words_ns.append(word)
     # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)
