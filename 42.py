def fact(n):
    if n == 0 :
        return n * fact(n-1)

num = fact(5)
print(num)