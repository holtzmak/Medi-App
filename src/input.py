from typing import Counter
from unittest.result import failfast
from spellchecker import SpellChecker


def get_symptoms_from_input(sting):
    userList = sting.split()
    counter=0

    spell=SpellChecker()
    misspelled=spell.unknown(userList)
    for word in misspelled:
        Counter = Counter +1
    if(Counter!=0):
        print ("Your input have error in it.... Exiting")
        return None
    else: 
        
        return userList

def get_symptoms_from_user():
    print("Enter the list of Symptoms by space: ")
    i =input()
    while (function(i) == None):
        print("Input symptoms again")
        i =input()
        function(i)

    if(function(i) != None):
        userList=function(i)
        print ("The Symptoms are: ",userList)

get_symptoms_from_user()
