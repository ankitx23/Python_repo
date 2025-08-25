#Exercise 7: Find the number of occurrences of a substring in a string
#Write a Python code to find how often the substring “Emma” appears in the given string.



str_x = "Emma is good developer. Emma is a writer"
word = str_x.split()
count = 0

for word in word:
    if word =="Emma":
        count +=1
        print ("it came")
    