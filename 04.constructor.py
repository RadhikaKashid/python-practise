class EmployeeForBnp:
    city='Mumbai'
    def __init__(self,name,join_DT,city):
        self.name = name
        self.join_DT=join_DT
        self.city=city
       
    

    def printObj(self):
        print(f'the name is {self.name}')
        print(f'the join_DT is {self.join_DT}')
        print(f'the city is {self.city}')  
        
    @staticmethod
    def greet():
        print('Good Day!!')


a=EmployeeForBnp('radhika','2022-08-29','Kochi')
b=EmployeeForBnp('pragati','2022-08-29',"goa")
a.printObj()
b.printObj()
