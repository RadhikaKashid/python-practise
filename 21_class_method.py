# class Person:
#     name='ananymous'

#     def changeName(self,name):
#         self.name=name

# p1=Person()
# p1.changeName('radhika kashid')
# print(p1.name)
# print(Person.name)
'''
class Person:
    name='ananymous'

    def changeName(self,name):
        self.__class__.name= 'Rahul'

p1=Person()
p1.changeName('Rahul')
print(p1.name)
print(Person.name)
'''
class Person:
    name='ananymous'

    @classmethod # using this method we can change directly into the class attributer
    
    def changeName(cls,name):
        cls.name= 'Rahul'

p1=Person()
p1.changeName('Rahul')
print(p1.name)
print(Person.name)
