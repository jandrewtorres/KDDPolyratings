# Name: John Torres and Ryan Gelston
# Class: CSC 466
# Assignment: Term Project
# Description: Reads ratings from sql database and turns each entry into a 
#  dictionary object

"""
Data schema:

{
   "Date" : ,
   "Required" : [True | False],
   "Course" : , 
   "Class" : "String",
   "Score" : number
   "Lecturer" : "String",
   "Grade" : ,
   "Review" : [["String",...], ...]
}


General Process For Review Processing:
   Import reviews and metadata from SQL database |
   Remove punctuation and invalid words |
   Stem words in reviews, maintian order 

   In stemmed reviews find words/phrases that strongly correlate 
   with a particular score

   Create shema for word vector based on correlations

    
"""

import sqlite3
import nltk.tokenize as MWETokenizer
from nltk.stem.lancaster import LancasterStemmer

db_key = {
   'fdsa' : "Date",
   'fdsd' : "Required",
   'fdsa' : "Course",
   'fdsa' : "Class",
   'fdsa' : "Lecturer",
   'fdsa' : "Grade",
   'fdsa' : "Review"}


def createRecords():
   

def sqlToDict(cursor):
   """ sql cursor --> [{'col': row_value},...] 
      Taken from alecxe's answer to SO question #28755505
      It's so tiny an elegent!!!""" 
   desc = cursor.description
   column_names = [col[0] for col in desc]
   return [dict(itertools.izip(column_names, row
            for row in cursor.fetchall()]


def cleanData(data, key_schema):
   """ Cleans data from raw SQL dict format """

   data = changeKeys(data, key_schema)

   for rec in data:
      rec['Review'] = cleanReview(rec['Review'])

   return data
   

def changeKeys(data, key_schema):

   for record in data:
      for key in key_schema:
         record[key_schema[key]] = record.pop[key]

   return data

def cleanReview(review):
   """
      
   """

   sent_tknzr = TweetTokenizer()
   stemmer = LancasterStemmer()

   return [[list(map(lambda w: stemmer.stem(w), tkn_sent))
               for tkn_sent in sent_tknzr.tokenize(sent)]
            for sent in rec_tknzr.totenize(review)]
           

def tokenizeRecord(record):
   """ "String" --> [["String",...],...] """
   return [tokenizeSentence(sent) for sent in splitSentences(record)]


def tokenizeSentence(sentence, tokenizer):
   """ "String" --> ["String", ...] """
   sentence = tokenizer.tokenize(sentence)
   return[stemmer.stem(word) for word in sentence]

      

