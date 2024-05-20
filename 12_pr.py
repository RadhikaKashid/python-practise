'''create account class with 2 attributes-balance and account no
Create meyhods for debit, credit and printing the balance'''


class Account:
    def __init__(self,acc,bal,d_amount,c_amount):
        self.bal=bal
        self.acc=acc
        self.d_amount=d_amount
        self.c_amount=c_amount

    
    def debit(self):
        print(f'your account is debited with {self.d_amount} rupee')

    def credit(self):
        print(f'your account is credited with {self.c_amount} rupee')

    def get_bal(self):
        # self.f_bal=f_bal
        self.bal= self.bal+self.c_amount-self.d_amount
        print(f'final balance of {self.acc} is {self.bal}')


acc1=Account('radhika',3000,500,200)
acc1.debit()
acc1.credit()
acc1.get_bal()
