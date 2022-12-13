list1=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
list2=[]
for j in list1:
    if type(j) is list:
        for i in j:
            list2.append(i)
    else:
        list2.append(j)
print(list2)
