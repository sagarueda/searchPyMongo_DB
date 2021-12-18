# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:05:46 2021

@author: SaGaRueda
"""

import pymongo

import funciones


def main():
    client = pymongo.MongoClient("mongodb://chirimoya0:huilen03@cluster0-shard-00-00.udzpg.mongodb.net:27017,cluster0-shard-00-01.udzpg.mongodb.net:27017,cluster0-shard-00-02.udzpg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-w2m870-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.MBD2021
    collection = db.loddata
    collection_user = db['users']                  

    usuario = funciones.signUp()#users.User(i_name,i_email,i_pass,i_bd)      

    collection_user.insert_one({
                '_id':usuario.email,        
                'name' : usuario.name,        
                'password': usuario.password,
                'birthday':usuario.birthday,
            })        
    name = funciones.signIn(collection_user)   
    
    
    funciones.searchBy(collection,name)    
             
    
    
if __name__ == "__main__":
        main()