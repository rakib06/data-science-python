"""

#from import_modules_modules_the_standard import find_index as fi,test
#import import_modules_modules_the_standard as my_module #er sathe related
from import_modules_modules_the_standard import *
courses=['History','Math','Physics','CompSci']
index=find_index(courses,'Math')
print(index)


print(test)

"""

""" sys 
from import_modules_modules_the_standard import find_index as fi,test
import sys
print(sys.path)
"""
#path onno folder a thakle 

"""
import sys
sys.path.append('D:/#2018/#Machine Learning/coding')
print(sys.path)


print()
"""
####other function

import random 
courses=['History','Math','Physics','CompSci']
random_course =random.choice(courses)
print(random_course)


import math
rads=math.radians(90)
print(rads)
print(math.sin(1.57))
print()


import datetime
import calendar
today=datetime.datetime.today()
today=datetime.date.today()
#today=datetime.time.now() #hbe na
print(today)
print()
print(calendar.isleap(2020))


import os
print(os.getcwd()) #current file directory 


print(os.__file__) #os er kothay run hosse 

#browser access
import antigravity