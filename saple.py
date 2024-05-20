import math
import os
import random
import re
import sys


n = random.randint(1,101)
print(n)
if n%2 !=0:
    print('Weired')
    
elif n%2==0 and 2<=n<=5:
    print('Not Weired')
elif (n%2==0) and (6<=n<=20):
    print('Weird')
else:
    print('Not Weired')
