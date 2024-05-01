my_list=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
sum=0
big=my_list[0]
for i in my_list:
    for j in range(len(my_list[i])):
        sum+=my_list[i][j]
        if sum>big:
            big=sum
print(big)    