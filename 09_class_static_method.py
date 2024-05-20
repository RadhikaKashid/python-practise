class Student:
    sub1='maths'
    sub2='sci'
    sub3='eng'
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3

    @staticmethod #decorator
    def hello():
        print('Hello')

    def average(self):
        avg=(self.marks1 + self.marks2 + self.marks3)/3
        print(f'avrage of marks for {self.name} is {avg}' )


s1=Student('radhika',50,78,98)
s1.hello()
s1.average()