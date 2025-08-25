# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.


# list = [11,222,3333,44,33,22,33,11]
# list2 = [11,222,3333,44,33,22,33]


# print(len(list))
# print(len(list2))

# if list[0] == list[7]:
#     print (True)
# else:
#     print (False)

# if list2[0] == list[6]:
#     print (True)
# else:
#     print (False)


def firstlastsame(number):
    print (number)
    firstnumber = number[0]
    lastnumber = number[-1]

    if firstnumber == lastnumber:
        print (True)
    else:
        print(False)

x =(11,222,3333,44,33,22,33,11)
print (firstlastsame(x))