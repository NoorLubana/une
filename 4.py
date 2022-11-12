def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def divi(a,b):
    print(a/b)

a=int(input("First Number:"))
b=int(input("Second Number:"))
c=str(input("operator: "))
if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="*":
    multi(a,b)
elif c=="/":
    divi(a,b)
