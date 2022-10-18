num1=int(input("First Side:"))
num2=int(input("Second Side:"))
num3=int(input("Third side:"))
s=(num1+num2+num3)/2
area=(s*(s-num1)*(s-num2)*(s-num3))**0.5
print(area)