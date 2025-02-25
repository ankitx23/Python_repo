#assign list to a list, it should be always in square bracket
#list = [1,2,3,4,7,9,0]
#print (list)
#print (type(list))

#function to add the numbers in list

#a= sum(list)
#print (a)

# python is flexible with adding any type of item in the list like you can add int, float, string , char

b =[3,4,6,7,"d", 4.9, "adsjkhg"]
#print (b)

#function to update item in a given list by using indexing using above list

#print (b[0])
                #modify the list

b[0]=78

#print (b)

#print the average/mean of a llist

c= [34,45,56,67,78,89,90,1,12,23]

e= len(c)
d= sum(c)
f= d/e

print (f) #avg 
#to print the sum of a list
print (d)
#to print the max from a list
print (max(c))
#to print the minimum value of a list
print (min(c))

#enumerate
#print (list(enumerate(c))) #this prints the index with the value of list


#zip function #should ve same quantity

t= [1,2,3,4,5,6]
u= ['a','b','c','d','e',"f"]

print (list (zip(t,u)))


#count repeatitive numbers in a list
z= (1,2,3,4,545,5,4,4,5,4,4,4,7)

count = z.count(4)
print ("count of element 2 is : ", count)
