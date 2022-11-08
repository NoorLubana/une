a=float(input("first side:"))
b=float(input("Second side:"))
c=float(input("third side:"))
s=(a+b+c)/2
areaOfTriangle=(s*(s-a)*(s-b)*(s-c))**0.5
print(areaOfTriangle)