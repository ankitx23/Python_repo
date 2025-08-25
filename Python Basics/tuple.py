#diff between tuple and loist - you cant modify tuple but you can modify list and USE Parenthesis().

a= (1,2,3,4,5,56,67,7,9)

b= type(a)
#print (b)

# lets try to update an element (doesnt work)

#print(a)
#a(0) = 45
# print (a)

#convert tuple into list
newlist = list(a)

#print (newlist)

#can store anything in a tuple+ 

f= (1,"m","ankit",56,3,59)
#print (f)

#adding two tuple

g = f+a
print (g)



