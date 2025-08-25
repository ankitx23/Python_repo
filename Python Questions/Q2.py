#Write Python code to iterate through the first 10 numbers and, in each iteration, 
#print the sum of the current and previous number.


a=0
b=0

while a<10:
    
    while b<a: 
        b+=1
    a+=1
    print (f"the sum of {a} and {b} is ",a+b)

    

previous = 0
current = 0

while current < 10:
    print(f"Current number: {current}, Previous number: {previous}, Sum: {current + previous}")
    previous = current
    current += 1
