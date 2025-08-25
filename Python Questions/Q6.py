# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55


y=[10, 20, 33, 46, 55]

for i in y:
    if i%5==0:
        print(f" {i} is divisible by 5")
    else:
        print (f" {i} is not divisble by 5")

