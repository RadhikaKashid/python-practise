class Account:
    def __init__(self,acc,bal):
        self.bal=bal
        self.acc=acc
        # self.amount=amount
        

    
    def debit(self, amount):
        self.bal -= amount
        print(f'your account is debited with {amount} rupee')
        print(f'balnace of {self.acc} is {self.bal}')

    def credit(self, amount):
        self.bal += amount
        print(f'your account is credited with {amount} rupee')
        print(f'balnace of {self.acc} is {self.bal}')

    def get_bal(self):
       return self.bal

acc1=Account('radhika',3000)
acc1.debit(100)
acc1.credit(400)
acc1.get_bal()
