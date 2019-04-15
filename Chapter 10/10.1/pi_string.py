# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:14:38 2019

@author: Administrator
"""

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
   print("Your birthday is in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")