# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 13:59:55 2021

@author: reema
"""

#_*_coding: utf-8 -*-
"""
Created on Sat Jul 10 12:11:13 2021
@author: Lenovo
"""

# Python 3 program to find
# factorial of given number
def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))