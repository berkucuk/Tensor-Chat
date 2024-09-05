import subprocess as sub
import os
import pyrebase
import json
import numpy as np
import time
import subprocess
from firebase import firebase
from focal_loss import BinaryFocalLoss
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Dense, LSTM, Embedding
from keras.layers import Dropout, Activation, Bidirectional, GlobalMaxPool1D
from keras.models import Sequential
from keras import initializers, regularizers, constraints, optimizers, layers
from keras.preprocessing import text, sequence
import tensorflow as tf
from keras import models
from keras import layers
from keras import optimizers

j=0
i = 0
config = {
        "apiKey": "AIzaSyBMi6Ubsol82cMe_p2hUdP8nu1efKUHRAw",
        "authDomain": "bogazici-8cc64.firebaseapp.com",
        "databaseURL": "https://bogazici-8cc64-default-rtdb.firebaseio.com",
        "projectId": "bogazici-8cc64",
        "storageBucket": "bogazici-8cc64.appspot.com/",
        "messagingSenderId": "1087034936639",
        "appId": "1:1087034936639:web:6dd6ba18831e23841d178a",
        "measurementId": "G-M40JQ2MNTX"}

def storg():
    text = []
    firebase_storage = pyrebase.initialize_app(config)
    strg = firebase_storage.storage()
    allFiles = storage.list_files()

    for file in allFiles:
        print(file)
        text.append(file.name)
        try:
            storage.child(text[i]).download("Photos/"+i+".jpg")
            i+=1

        except:
            print("[-]İmage Not Found")


try:
    firebase = firebase.FirebaseApplication('https://bogazici-8cc64-default-rtdb.firebaseio.com/', None)
    result = firebase.get('https://bogazici-8cc64-default-rtdb.firebaseio.com/messages/', '')
    list2 = []

    items = result.items()
    for key , value in items:
        list2.append(key)

    #print(list2)
    url=('https://bogazici-8cc64-default-rtdb.firebaseio.com/messages/'+list2[j]+"/text/")
    result2 = firebase.get(url, '').items()
    #result3 = result2.items()
    print(url)
    print(result2)

    values=[]

    for value in result2:
        values.append(value)
        j+=1



except:
    print("[-]Value Not Found")

"""
while True:
    #storg()
    DB()
    time.sleep(0.25)
"""
