#Integers are Immutable

num1 = 11
num2 = num1


print (num1, id(num1))
print (num2, id(num2))

num2 = 23
print (num1, id(num1))
print (num2 , id(num2) )

#Dictionaries are mutable

a = {
        'value' : 39
    }

b = a

print (a, id (a))
print (b , id(b))

b ['value'] = 49

print (a, id(a))
print (b, id(b))