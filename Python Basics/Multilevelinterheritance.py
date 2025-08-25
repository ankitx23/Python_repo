class Car:
    @staticmethod
    def start():
        print ("car started..")

    @staticmethod
    def stop():
        print ("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

class Fortuner (ToyotaCar):
    def __init__(self,type):
        self.type = type


car1= Fortuner("Deisel")
car1.start()