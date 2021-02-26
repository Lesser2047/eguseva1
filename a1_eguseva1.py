#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_eguseva1.py
Author: Elizaveta Guseva
The python code in this file (a1_eguseva1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

# The function leap_year() checks if the year entered is a leap year or not

def leap_year(obj):
    newobj = int(obj)
    
    if newobj%4 != 0:
        result = False
    else:
        if newobj%100 != 0:
            result = True
        else:
            if newobj%400 != 0:
                result = False
            else:
                result = True  

    return result

# Tje function goes through all the characters in the obj1 and compares them to the carracters in the obj2. If the character is not in the obj2 it is not getting written to a variable, that is returned.

def sanitize(obj1,obj2):
    newthing = ''
    letter = ''        
    newobj1 = list(obj1)
    for letter in obj1:
        if letter in obj2:
            newthing += letter
    results = str(newthing)
    return results

# The function checks if the user input value is as long as defined in intobj 

def size_check(obj, intobj):
    
    lenght = len(obj)
    if lenght == intobj:
        status = True
    
    else:
        status = False

    return status

# The function checks if the user input value is within the two values that are fefined in obj2

def range_check(obj1,obj2):
    
    obj2split1 = str(obj2).strip('()') 
    obj2split = obj2split1.split(',')
    MIN_VALUE, MAX_VALUE = obj2split[0], obj2split[1] 
    intobject1 = int(obj1)

    if ((int(MIN_VALUE) <= intobject1) and (intobject1 <= int(MAX_VALUE))):
        status = True
    else:
        status = False

    return status
    
# The function prints the usage of the algorithm if user input too many values

def usage():    
    
    status = 'Usage: a1_eguseva1.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD'

    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  
