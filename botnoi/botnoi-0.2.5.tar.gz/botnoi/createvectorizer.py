#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
######
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

import pandas as pd

styledb = pd.read_pickle('allstyle.p')

def sentokenize(sentence):
    return list(sentence)

def trainsentencemod(outmod='mod.p'):
  trainsentence = styledb['Keyword'].astype('str').values 
  vectorizer = TfidfVectorizer(tokenizer=sentokenize,max_features=10000,decode_error='ignore',ngram_range=(0, 5))
  vectorizer.fit(trainsentence)
  pickle.dump(vectorizer,open(outmod,'wb'))

#vec = pickle.load(open('mod.p','rb'))

def encodesentence(sentence):
    return vec.transform(sentence)


#def createvectorizer():

