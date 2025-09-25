_________________Python test 2____________________
!Q.1
01 import os

02 def read_file(file):

03     line = None

04     if os.path.isfile(file):

05         data = open(file, 'r')

06     while line != '': #incorrect line maybe because while should be in if block?

07         line = data.readline() #incorrect line

08         print(line) #incorrect line

!Q.4
p = 2
while p <= 100:
    is_prime = True
    for i in range(2,p):
        if p % i == 0: # finds factors
            is_prime = False
            break # moves onto the next number and doesn't print
        if is_prime == True:
            print(p)
            p=p+1 # moves onto next number

!Q.8
type(+1E10) # float because E is exponent
type(5.0) # float
type("True") # String
type(True) # Boolean

!Q.10
List operations in order:
    Parenthesis, Exponents, Unary positive/negative/not, Multiplication and Division, Add and Subtract, And
    Please Enter UnMinceD And Abnormal

!Q.13
import math
l =[str(round(math.pi)) for i in range (1, 6)]
print(l) # each i 1-6 is turned into 3.14.. then turned to int (3) then 'str'

!Q.22
employee_number = "sentinel"
parts = " "
while employee_number != "":
valid = True
      employee_number = input("Enter employee number (ddd-dd-dddd) : ")
      parts = employee_number.split('-') # splits employee_numbers into 3 parts by '-'
      if len(parts) == 3:

           if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4: # first, second, third part

                if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
valid = True

      print(valid)

!Q.
