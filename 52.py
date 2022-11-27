number=[1,2,3,4,5,2,6]
b=[]
for i in range(0,len(number)-1):
    if number[i]==2:
        number.pop(i)
        number.insert(i,200)
print(number)