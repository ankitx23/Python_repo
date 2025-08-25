#Normal slicing #it starts with zero from left side and from right to left is starts from -1

string = "ANKIT, COMPUTER SCIENCE"

#retrieve the index of substring in a string

index= string.find("ANKIT")
print (index)

#using count on string
count = string.count()
print (count)



#print (len(string))
#print (string[0:6])
#print (string[7:])
#print (string[:-1])


#Slicing with STEP - in this we use step to skip in between string
#print (string[0:23:2]) # this will skip every 3rd. lettter


# reversing string in python using slicing
#print (string [::-1])

#pulling CNEI from string
#print (string[-6:-2])

#------TUPLE-------#

tuple = ("Computer",1,2,3,5,6,7)
#print (tuple[0])
#print (tuple[0:7])
#print (tuple[0:7:2])

#---------LIST-------#

list=[1,2,3,4,55,6,7,8,97,4]
#print (list[0::2])

#----------Dictionaries---------# IT doesn t support sliciing but y0ou can use subset to take keys out of Dictionary

dict = {"Name": "Ankit", "Class" : "Computer Science", "Subject" : "Programming"}
#print (dict[0:1])







