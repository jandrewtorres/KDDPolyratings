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
   "Department": "String",
   "CourseNum" : department, 
   "Class" : string,
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

import nltk
import sqlite3
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize 
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
   """ Swaps keys given a dictionary of the form 'old_key' : "new_key" """

   for record in data:
      for key in key_schema:
         record[key_schema[key]] = record.pop[key]

   return data


def cleanReview(review):
   """ Converts review into a list of lists of stemmed words """   

   #sent_tknzr = RegexTokenizer()
   stemmer = LancasterStemmer()

   return [[list(map(lambda w: stemmer.stem(w), tkn_sent))
               for tkn_sent in nltk.word_tokenize(sent)]
            for sent in review.split('.')]

#####################################################################
# Processing and filtering of data #
#####################################################################

def flattenReviews(data):
   """ Takes all the words in the reviews of a list of data points
         and puts them all in a list. 
       [{dataDict}, ...] --> ["string", ...] """
   return [word for review in data for word in review['Review']]

def flattenReview(review):
   """ Takes all of the words in a review and puts them in a list 
       [["string", ...], ...] --> ["string", ...] """
   return [word for sent in review for word in sent]

def filterLecturer(data, lecturer):
   """ Returns list of data dicts of a certain lecturer """
   return list(filter(lambda r: r['Lecturer'] == lecturer, data))

def filterOutLecturer(data, lecturer):
   """ Returns data entries not for a certain lecturer """
   return list(filter(lambda r: r['Lecturer'] != lecturer, data))

def filterDepartment(data, department):
   """ Returns data entries about a particular department """
   return list(filter(lambda r: r['Department'] == department, data))

def filterOutDepartment(data, department):
   """ Returns data entries about a particular department """
   return list(filter(lambda r: r['Department'] != department, data))

def filterRating(data, rating):
   " Returns data entries with a particular rating """
   return list(filter(
            lambda r: r['Rating'] >= rating && r['Rating'] < rating+1, 
            data))

def filterOutRating(data, rating):
   return list(filter(
            lambda r: not(r['Rating'] >= rating && r['Rating'] < rating+1),
            data))
