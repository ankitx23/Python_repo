#convert int into string
a= 5
b= str(a)
print (b, type(b))

#covert string into int 
#works only when there are integers in the string
c = "567"
d= int(c)
print (d, type(d))

#list to set
e= [1,2,3,4,5,5,56,7,8,0]
f= set(e)
print (type(f), type(e),f)

#set to list
g= list(f)
print (g, type (g))


#print lentth of list
print (len(g))
#print index of an element from the list
print (g.index(56))

