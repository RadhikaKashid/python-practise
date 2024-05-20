class Student: # class contains data(attributes) and methods(functions)
    collage_Name='PVPIT'
    name='anonymous'  
    def __init__(self,name,marks) :   # functions in a class known as methods
        self.name=name  
        self.marks=marks
        print("adding a new student in database")

    def welcome(self):
        print(f'Welcome students {self.name}')

    def get_marks(self):
        return self.marks

s1=Student('ram',56)

print(s1.name,s1.marks, s1.collage_Name)
s1.welcome()
print(s1.get_marks())