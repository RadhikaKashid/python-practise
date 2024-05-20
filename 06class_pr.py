class Student:
    collage_Name='PVPIT'
    name='anonymous'  # class atributes (variable of class common for all objects)
    def __init__(self,name,marks) :   # constructor
        self.name=name  #object atributes (different for different objects)
        self.marks=marks
        print("adding a new student in database")

s1=Student('ram',56)

print(s1.name,s1.marks, s1.collage_Name)