def to_two(a):
    k=0
    while a>1:
        c=a%2
        a=a//2
        k=k*10+c
    rez1=k*10+1
    o=0
    while rez1>0:
        j=rez1%10
        o=o*10+j
        rez1=rez1//10
    return o
a=int(input())
print(to_two(a))