salary=int(input("current salary:"))
yearsworking=int(input("years working:"))
if yearsworking>=10:
    print("New salary is:",salary+salary*0.1)
elif yearsworking>6 and yearsworking<10:
    print("New salary is:",salary+salary*8/100)
elif yearsworking<=6:
    print("New salary",salary+salary*5/100)