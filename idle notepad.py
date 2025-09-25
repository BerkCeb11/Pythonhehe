01 import os

02 def read_file(file):

03     line = None

04     if os.path.isfile(file):

05         data = open(file, 'r')

06     while line != '': #incorrect line maybe because while should be in if?

07         line = data.readline() #incorrect line

08         print(line) #incorrect line

