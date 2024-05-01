
list1=[1,3,5,7,9,10]
list2=[2,4,6,8]
n=len(list1)
list1.pop(n-1)
for i in list2:
    list1.append(i)
print(list1)