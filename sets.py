#unordered collection of unique elements
#no duplicates
# sets are mutable

#create a non empty set
emptyset  = set()
#print (type(emptyset))

# create a non empty set within curly braces

#set = {1,2,3,4,'sdf'}
#print (type(set))

#mutability 
#set.add(7)
#set.add('goa')

#set.remove(2)
#print ((set))


#changing list to set
list1= [1,2,3,3,4,4,5,56,4,6,7,78,78,78,98,6,5,3]
set1= set(list1)

print (set1) #repeated values will be shown as single item, it can not have multiple items
