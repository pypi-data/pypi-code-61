''' Importing necessary libraries for chatbot.
All libraries are installed with their correct versions, while installing this library
Libraries used below are:

os: for interacting with os
nltk: massive tool kit to help with entire Natural Language Processing
string: for some utility functions
random : for random selections of responses
warnings: to supress all warnings
wikipedia : to get responses from wikipedia pages
numpy :used for working with arrays when text is converted to vector form
textblob : used for sentiment analysis
word_tokenize from nltk : used for ease of tokenization
chatterbot : heavily used to train the chatbot and get response
nltk.corpus : util module, to get stopwords, punct and wordnet
nltk.chat.util : another util from nltk
validate_email : to validate email
chatterbot_trainers: to train chatbot
sklearn : used for TFID for finding similarities using vectors
'''

import os    
import nltk             
import string
import random
import warnings
import wikipedia
import numpy as np
from textblob import TextBlob
from nltk import word_tokenize
from chatterbot import ChatBot
warnings.filterwarnings("ignore")
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections
from validate_email import validate_email
from chatterbot.trainers import ListTrainer
from sklearn.metrics.pairwise import cosine_similarity
from chatterbot.trainers import ChatterBotCorpusTrainer
from sklearn.feature_extraction.text import TfidfVectorizer


'''Some predefined list and responses'''

greeting_inputs =    ("hello","hi","greetings","greeting","sup","Wsup","what's up","hey","heya","hey","hi there","heloo","heelo")
greeting_responses  =   ["Hey","Hello","Hi there","How may I help you ?","Wsup, Hope you are doing well !","What's up","How may I help you ?"] 
wrong_responses =   ["Hmm Hmm, Tell me more!!","OK Can You Specify more ?","I don't Understand", "Tell me more ","OK, I see !!" ]
thank_you  =    [ "thank u", "thank you","thanx","thanks","thank","thnx","tnx" ]
ok_yes    =   [ "ok","k","kk","kkk","ook","okk","yes","sss","s","ss"]
referring  =    [" Is it right ?"," Is this what you want to know !!"," R8t ?","Is this what you are referring  ?"]
no =   ["no","noo","nah","nooo"]
ok_yes_resp=[" How Can I help you ?","Anything I can help you with ?","How can I serve You ?","Need Help in Anything ?"]

'''Functions for formal reponses to give responses from above list randomly'''

def greeting(sentence):
        for word in sentence.split():
                if word.lower() in greeting_inputs:
                        return random.choice(greeting_responses)

def thank_u(sentence):
        for word in sentence.split():
                if word.lower() in thank_you:
                        return random.choice(thank_you)

def k_s(sentence):
        for word in sentence.split():
                if word.lower() in ok_yes:
                        return random.choice(ok_yes)


class Jigbot():
        '''Creating object with Jigbot requires to pass in the file and name for chatbot while initialing'''
        
        def __init__(self, txt_file, name="Jiganesh"):
                self.name = name
                self.botspeech = name + ":  "
                self.txt_file = txt_file

        ''' Function to get data from users used to retreive name, email and number of user, Records and returns this information.'''
        
        def get_data(self):
                print(self.botspeech, "Please Fill your details for better Reach  !")
                bname, bemail, bnumber = True, True, True

                while bname:
                        print(self.botspeech, "Name format:  Input Name Middle name Surname")
                        name_of_person = input("User:  ")  # name_recorded
                        if len(name_of_person.split(" ")) >= 3:
                                bname = False

                while bemail:
                        print(self.botspeech, "Enter your email address")
                        address = input("User:  ")  # email is recorded
                        check = validate_email(address)
                        if check == True:
                                bemail = False

                while bnumber:
                        print(self.botspeech, "Enter your 10- digit Contact Number")
                        contact = input("User:  ")  # contact recorded
                        if len(contact) >= 10 and len(contact) <= 13 and contact.isdigit() == True:
                                bnumber = False
                print(self.botspeech, "Thank You")

                return name_of_person, address, contact


        

''' Functions using textblob to give sentiment analysis of the text provided '''
def sentiment(text):
        ''' Function returns seniment score for polarity as well as subjectivity'''
        text = str(text)
        return Textblob(text).sentiment

def polarity(text):
        ''' Function returns sentiment score for polarity only'''
        text=str(text)
        return Textblob(text).sentiment.polarity

def subjectivity(text):
        ''' Function returns sentiment score for subjectivity only'''
        text=str(text)
        return Textblob(text).sentiment.subjectivity
