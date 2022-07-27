'''#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    swap=sentence.swapcase()
    newlist=list(swap.split())
    string=''
    for i in range(len(newlist)-1,-1,-1):
        string=string+newlist[i] +" "
    return string
   

if __name__ == '__main__': '''
'''
for x_ in range(max(0,x-1),min(height,x+2)):
      for y_ in range(max(0,y-1),min(width,y+2)):
             if (x,y)==(x_,y_): continue
    # do stuff with the neighbours

 a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 width=height=3 x,y=0,2
 for x_ in range(max(0,x-1),min(height,x+2)):
   for y_ in range(max(0,y-1),min(width,y+2)):
     if (x,y)==(x_,y_): 
         continue
            print a[x_][y_]

'''