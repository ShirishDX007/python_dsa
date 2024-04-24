import math
import os
import random
import re
import sys

n = int(input("Enter an integer: "))

if n % 2 == 1:
    print("weird ")
elif n % 2 == 0 and 2 <= n <= 5:
    print("not weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and  n > 20:
    print("Weird")    

if __name__ == '__main__':
    n = int(input().strip())

          
        
