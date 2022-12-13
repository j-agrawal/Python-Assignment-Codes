list=[]
no_of_ele=int(input("enter number of elements:"))
for i in range(0,no_of_ele):
    string=(input())
    list.append(string)
print(list)
num=list[0]
temp=0
for i in list:
    temp=max(temp,list.count(i))
    if(list.count(i)==temp):
        num=i
for i in range(0,temp):
    list.remove(num)
temp=0
num=list[0]
for i in list:
    temp=max(temp,list.count(i))
    if(list.count(i)==temp):
        num=i
print(num)
