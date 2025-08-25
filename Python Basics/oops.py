#def __init__ (self,full name):
 #   self.name = full name

#def hello (self):
 #   print("hello",self.name)

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student ("ANKIT")
print (s1.name)
del (s1.name)
print (s1.name)