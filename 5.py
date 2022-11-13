a=int(input("First side:"))
b=int(input("Second side:"))
c=int(input("Third side:"))
s= (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)