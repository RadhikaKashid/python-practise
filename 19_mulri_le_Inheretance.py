class A:
    var1='Welcome to class A'

class B:
    var2='welcome to class B'

class C(A,B):
    var3='welcome all sudents'

a= C()
print(a.var1)