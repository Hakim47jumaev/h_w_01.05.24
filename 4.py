list1=input().split()
cnt=0
li=["0"]
for i in list1:
    if i=="0":
        list1.remove(i)
        cnt+=1
for i in range(cnt):
    list1.append(li[0])
print(list1)