def mul(a,*b):
    for i in b:
        a *=i
    return a

print(mul(1,2))
print(mul(2,4,6))
print(mul(3,5,7,11))
