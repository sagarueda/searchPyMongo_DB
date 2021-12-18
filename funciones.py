# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 00:50:19 2021

@author: SaGaRueda
"""

#funciones auxiliares

import users
import pymongo
from pymongo import MongoClient
import re
import dates
import funciones
from datetime import date
from dateutil.relativedelta import relativedelta
from pprint import pprint

def validation(name,mail,bd):
    """chequear name string
     #chequear email tenga @aaa.com
     #chequear birthday format"""
    return 1



def signUp():
    """This function ask the information of a new user and return an object of "User" class """
    print(80*"-")
    print("SIGN UP")
    print(80*"-")
    i_name = input("What is your name?\n")
    i_email = input("What is your email?\n")
    i_pass = input("Write a password\n")
    i_bd = input("What is your birthday (Format day,month,yyyy)\n")
    i_bd = [int(x) for x in i_bd.split(",")]
    
    usuario = users.User(i_name,i_email,i_pass,i_bd)
    
    return usuario



def signIn(collection):
    """This function ask the email and the key of a user and look in the database if the key
    match with the key that was uploaded in the data base, if it is wrong, it says bye"""
    print(80*"-")                 
    print("SIGN IN")
    print(80*"-") 
    email = input("enter your email?\n")
    key =  input("enter your password?\n")    
    
    client = collection.find({"_id": email})
    
    for i in client:
        if str(i["password"]) == key: 
            print ("Hello",i["name"])
            usuario = users.User(i["name"],email,key,i["birthday"])
            usuario.daysTillBd()
            return usuario.name
        else :
            print("your password is incorrect bye!")
            exit
            return 0
        
        
def searchBy(collection,name):
    i = 0
    while i not in [1,2,3]:
        print("\n",10*"-","Search by domain?",10*"-","Search by title?",10*"-","Exit")
        print(15*"-","press 1",20*"-","press 2",15*"-","press 3")
    
        i = int(input("Select your option\n"))
        if i not in [1,2,3]:
            print("Your option is wrong, choose a new number")
    #return i
    
    
    if i == 1 : searchByDomain(collection)
    if i == 2 : searchByTitle(collection)
    if i == 3 : 
        #print("Bye ",name)
        print("Bye ")
        return 1
    searchBy(collection,name)

    
def searchByDomain(collection):
    cursor = collection.find({})
    list_target = []
    for document in cursor:
        if (document['domain'] not in list_target) and (len(document['domain'])>0):
            list_target.append(document['domain'])
    
    option = 0
    print("your search is by domain\n\n")
    while option not in range(1,len(list_target)):
        
        print("These are the domains:\n")
        j=1
        for dom in list_target:
            print(j,"-->",dom)
            j+=1            
           
        option = int(input("Select yout option\n")) 
        
        if option not in range(1,len(list_target)):
            print("Your option is wrong, choose a new number\n")
        else: print("Your domain is: ", list_target[option-1])
    
        
    cursor = collection.find(
        {"domain":list_target[option-1]}
        )
    
    for document in cursor:
        pprint(document)
    
    #searchBy()    
        

        
 
def searchByTitle(collection):    
    
    print("your search is by title")
    text = input("enter your text:\n")    
    result = collection.aggregate([
    {
        '$match': {
            'title': re.compile(text )
        }
    }, {
        '$sort': {
            'triples': -1
        }
    }
    ])   
    
    print("\n",10*"-","Do you want to see all the fields?",10*"-","Only Id, title and triples?",10*"-")
    
    print(25*"-","press 1",35*"-","press 2",20*"-")
    i = int(input("Select your option\n"))
    
    if i==1:
        for doc in result:
            pprint(doc)  
    elif i == 2:        
        for doc in result:
            print("_id:     ", doc["_id"])
            print("title:   ", doc["title"])
            print("triples: ", doc["triples"],"\n")
            
                