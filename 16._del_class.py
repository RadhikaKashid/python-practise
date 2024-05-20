class MyClass:
    classy ='class value'

dd=MyClass()

print(dd.classy)

dd.classy='Instance value'

print(dd.classy)

del dd.classy

print(dd.classy)