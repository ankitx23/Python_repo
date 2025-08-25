# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Given 1:
# number1 = 20
# number2 = 30
# Expected Output:
# The result is 600

# Given 2:
# number1 = 40
# number2 = 30
# Expected Output:
# The result is 70

a = 20
b= 30
c= 40
d= 30

if (a*b) <= 1000:
     print ("the product is : ", a*b)
else:
     print ("the sum is: ", a+b) # returns 600

