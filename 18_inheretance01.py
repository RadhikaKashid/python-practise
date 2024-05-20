
class Car:   # parent class or base class
    def __init__(self, ):
        self.acc = False
        self.brk =False
        self.clutch = False

    def start(self):
        self.clutch=True
        self.acc =True
        print("car started..")

    @staticmethod
    def stop():
        print('car is stopped')


class Toyata(Car):  # inheretance----> child class or derived class


    def __init__(self,brand):
        self.brand=brand
        

class Fortuner(Toyata):
    def __init__(self,type) :
        self.type=type

car1=Fortuner('electric')
car2 =Toyata('perius')

car1.start()