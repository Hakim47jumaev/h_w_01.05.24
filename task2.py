def to_ten(a):
    b=len(a)
    h=int(a)
    h=int(a)
    res=0
    for i in range(0,b):
        c=h%10
        if c>1:
            return "Error"
        k=c*2**i
        res+=k
        h=h//10
    return res

a=input()
print(to_ten(a))

