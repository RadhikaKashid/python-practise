class student:
    def __init__(self, phy,chem, maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        # self.percentage=str((self.phy+self.chem+self.maths)/3)+'%'


       
    # def cal_percentage(self):
    #     self.percentage=str((self.phy+self.chem+self.maths)/3)+'%'

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+'%'







stu1=student(97,98,99)
print(stu1.percentage)

stu1.phy=86

print(stu1.percentage)
        