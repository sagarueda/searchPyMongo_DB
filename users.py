# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:19:51 2021

@author: SaGaRueda
"""
import dates
from datetime import date

class User(object):

    def __init__(self,nom="",mail="",passw="",bd=[]):
        self.name = nom
        self.email = mail
        self.password = passw
        self.birthday = bd

    def imprimir(self):
        print("Nombre",self.name,"email",self.email)
        
    def daysTillBd(self):
        cumple = dates.Dates(self.birthday[0],self.birthday[1],date.today().year+1)
        meses = -cumple.months(date.today().day, date.today().month, date.today().year)
        días = -cumple.days(date.today().day, date.today().month, date.today().year)
#        print(meses,días)
        if meses > 0 and días > 0 :
            print(" There are ", meses, "meses","and ", días, "days", "until your birthday!")
        elif meses == 0 and días > 0:
            print(" There are", días, "days", "until your birthday!")
        elif meses == 0 and días == 0: 
            print("Your birthday is today, happy birthday! " + self.name)
        


# bloque principal
if __name__ == "__main__":        
        
    persona1= User("Pedro","pedro@uma.es","pedro123",[1,1,1982])    
    persona1.imprimir()
    persona3 = User()
    persona3.name = "José"
    persona3.email = "jose@uma.es"
    persona3.password = "jose234"
    persona3.birthday = [17,12,1987]
    persona3.imprimir()    
    persona3.daysTillBd()