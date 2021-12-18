# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta


class Dates(object):
    
    def __init__(self, day, month, year):
        self.date = date(year, month, day)
        
    def total_days(self, day, month, year):
        toDate = date(year, month, day)
        delta = toDate - self.date
        return delta.days

    def days(self, day, month, year):
        toDate = date(year, month, day)
        rdelta = relativedelta(toDate, self.date)
        return rdelta.days
    
    def months(self, day, month, year):
        toDate = date(year, month, day)
        rdelta = relativedelta(toDate, self.date)
        return rdelta.months

    def years(self, day, month, year):
        toDate = date(year, month, day)
        rdelta = relativedelta(toDate, self.date)
        return rdelta.years

        
# bloque principal

#
if __name__ == "__main__":
    nacimiento = Dates(16, 1, 1991)
    print(nacimiento.total_days(date.today().day, date.today().month, date.today().year), "días vividos")

    años = nacimiento.years(date.today().day, date.today().month, date.today().year)
    print("    ", años, "años")
    meses = nacimiento.months(date.today().day, date.today().month, date.today().year)
    if meses > 0:
        print("    ", meses, "meses")
    días = nacimiento.days(date.today().day, date.today().month, date.today().year)
    if días > 0:
        print("    ", días, "días")
