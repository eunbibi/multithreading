# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:39:38 2021
@author: anna_eunbi
"""

# Python program to illustrate the concept of threading

# importing the threading module
import threading

    #function to print square of given num
def print_square(num):
    print("2^2= {}".format(num * num))
    
    #function to print cube of given num
def print_cube(num):
    print("2^3= {}".format(num * num * num))
  
if __name__ == "__main__":
    # creating thread
                          #target: the function to be executed by thread
    t1 = threading.Thread(target=print_square, args=(2,))
                                            #args: the arguments to be passed 
                                            #      to the target function            
    t2 = threading.Thread(target=print_cube, args=(2,))
  
    # start, t1
    t1.start()
    # start, t2
    t2.start()
  
    # wait for completing t1
    t1.join()
    # wait for completing t2
    t2.join()
  
    # t1 and t2 are completely executed
    print("t1 and t2 are executed")
    