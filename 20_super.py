class Car:  
    def __init__(self,type ):
        self.type = type
        
    @staticmethod
    def start():
        
        print("car started..")

    @staticmethod
    def stop():
        print('car is stopped')


class Toyata(Car):  
    def __init__(self, name, type):
        
        super().__init__(type)
        self.name=name
        super().start()


car1=Toyata('fortuner','electric')
print(car1.type)