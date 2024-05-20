class Account:
    def __init__(self,ac_no,pas):
        self.ac_no=ac_no
        self.__pas=pas

    def reset_pas(self):
        print(self.__pas)
        

ac1=Account('1234','12er')

print(ac1.ac_no)
print(ac1.reset_pas())

