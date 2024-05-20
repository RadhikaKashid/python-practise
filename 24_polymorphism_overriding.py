class Thought():
    def __init__(self) :

        pass
    def message(self):
        print('thought, alwyas come and go')

class Advise(Thought):
    def __init__(self):
        super(Advise,self).__init__()
    def message(self):
        print('Warning: Risk is always involved when you are dealing woith market!')

b=Thought()
print(b)