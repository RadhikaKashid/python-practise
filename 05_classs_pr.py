class person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        

    def printObj(self):
        print(f"persons name is {self.name} and age is {self.age}")

p1=person('ram',18)

# print(p1.name)
# print(p1.age)
print(p1.printObj())