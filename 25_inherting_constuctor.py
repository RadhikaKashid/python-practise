import random

class Animal():
    def __init__(self,name) :
        self.name=name

class Dog(Animal):
    def __init__(self, name): 
        super(Dog,self).__init__(name)
        self.breed=random.choice(['Doberman','Germeen shepherd','Beagle'])

    def fetch(self,thing):
        print('%s goes after the %s!'%(self.name,thing))

d=Dog('dogname')

print(d.name)
print(d.breed)