#unordered collection of unique elements
#no duplicates
# sets are mutable

#create a non empty set
emptyset  = set()
#print (type(emptyset))

# create a non empty set within curly braces

set1 = {1,2,3,4,'sdf'}
set2 = {4,5,6}


#print (type(set))

#mutability 
#set.add(7)
#set.add('goa')

#set.remove(2)
#print ((set))


#changing list to set
list1= [1,2,3,3,4,4,5,56,4,6,7,78,78,78,98,6,5,3]
set3= set(list1)

#print (set3) #repeated values will be shown as single item, it can not have multiple items


#set union intersection 
print ((set1 | set2) - (set1 & set2))
