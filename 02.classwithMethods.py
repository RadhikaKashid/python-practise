# A very basic sample class
class EmployeeForBnp:
    name='radhika'
    join_DT='2022-08-29'
    city='Mumbai'

    def printObj(self):
        print(f'the name is {self.name}')


a=EmployeeForBnp()  #a basic object
print(a.join_DT)
print(a.city)
a.printObj()

