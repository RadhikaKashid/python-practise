class Mother:
    def __init__(self,name):
        self.name=name
        print('i am the %s' %(self.name))
    
    

class Father():
    
    print('I am the father')

class child(Mother,Father):
    print('I am the Mother ')

issubclass(child,Mother) and issubclass(child, Father)
True


a=child()
print(a)