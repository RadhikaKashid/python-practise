
class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
            print('{0} eats {1}' .format(self.name,food))


class Dog(Animal):
    def fetch(self,thing):
        print('{0} goes after the {1}!'.format(self.name,thing))

    def show_affection(self):
         print('{0}wags tail'.format(self.name))

class Cat(Animal):
    def swatsring(self):
        print('%s shred the string!'%(self.name))

    
    def show_affection(self):
         print('{0} purrs'.format(self.name))

for a in (Dog('rover'),Cat('Fliffy'), Cat('Precious'),Dog('Scouts')): a.show_affection()