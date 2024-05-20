
class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
            print('%s is eating %s' %(self.name,food))


class Dog(Animal):
    def fetch(self,thing):
        print('%s goes after the %s!'%(self.name,thing))

class Cat(Animal):
    def swatsring(self):
        print('%s shred the string!'%(self.name))

d=Dog('ranger')
c=Cat('Meow')
d.fetch('ball')

d.eat('Dog Food')
c.eat ('cat food')
d.swatsring()
d.swatsring()