list=[]
no_of_ele=int(input("enter number of elements:"))
for i in range(0,no_of_ele):
    ele=int(input())
    list.append(ele)
print(list)
d=int(input("enter the no of positions to rotate:"))
list2=[]
for i in range(d,len(list)):
    list2.append(list[i])
for i in range(0,d):
    list2.append(list[i])
print(list2)
