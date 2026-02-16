import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print('Weird')
    elif n%2==0 and n in range(2,6):
        print('Not Weird')
    elif n%2==0 and n in range(6,21):
        print('Weird')
    elif n%2==0 and n>20:
        print('Not Weird')

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap=True
    
    return leap

year = int(input())
