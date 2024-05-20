# operator overloading is nothing but the operator overloading

class complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_num(self):

        print(self.real, 'i+',self.img,'j')

    
    def add(self,num2):
        NewReal=self.real+num2.real
        NewImg=self.img+num2.img
        return complex(NewReal,NewImg)
    

num1=complex(1,3)
num1.show_num()

num2=complex(2,5)
num2.show_num()

num3=num1.add(num2)
num3.show_num