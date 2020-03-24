# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:03:57 2019

@author: Josh Stiller
"""
class EmployeeData:
    _firstname = ""
    _lastname = "" 
    _address = ""
    _employeenumber = 0
    _birthdate = ""
    _hiredate = ""
    
    def __init__(self, firstname, lastname, address, employeenumber, birthdate, hiredate):
        self._firstname = firstname
        self._lastname = lastname
        self._address = address
        self._employeenumber = employeenumber
        self._birthdate = birthdate
        self._hiredate = hiredate 
        
        print("First Name:", self._firstname)
        print("Last Name:", self._lastname)
        print("Address:", self._address)
        print("Employee Number:", self._employeenumber)
        print("Birthdate:", self._birthdate)
        print("Hiredate:", self._hiredate, "\n")

    def __iter__(self):
        return self

    def __next__(self):
     self.EmployeeList
     
def main(): 
    EmployeeList = [ 
            EmployeeData("Joshua","Stiller","1235 University Blvd", 2589985, "7/16/99", "8/23/17"),
            EmployeeData("Michael", "Jordan", "35 Rich Dr.", 232323, "2/17/63", "4/30/15"),    
            EmployeeData("Dan", "Martin", "43 Poor Dr.", 5469871, "1/1/77", "4/14/17"),
            EmployeeData("Jake", "Moris", "34 Rynd Farm", 6987125, "5/16/89", "5/6/14")
            ]
    
        
if __name__=="__main__":
   main()