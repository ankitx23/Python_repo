#dictionary is stored in pair of key and value 
#dictionary is mutable and you can store tuple and list
#items in dictionaries are separted by ,


student = {
  "name": "Alice",
  "age": 20,
  "major": "Computer Science",
  "marks": [23,4,5,6,6,7,6,7,78,9],
  "phone": (7,4,6,23,47,8,23)
}

#get all the keys
x= student.keys()
print (x)
#get the values
y= student.values()
print (y)

#get both
z= student.items()
print (z)



#using get() to get age strom the dict
age = student.get("age")
print (age)



#printing name
a=student["name"]
#print (a)

#to update a key in dictionary
b= student["name"] = "Ankit";
#print (b)

#adding a element to dictionary
c= student["class"] = "5"

#print (student)

#remove an element
del student["marks"] 

#print (student)

#print all the keys
d= student.keys()
#print (d)

#print the values

e= student.values()
#print (e)

#print the items (keys with their values)

f=  student.items()
#print (f)


#copy in dictonary

new = student.copy()
print (new)

new.clear()
print (new)


