list1=[]
no_of_ele_in_list1=int(input("enter number of elements in list 1:"))
for i in range(0,no_of_ele_in_list1):
    string=(input())
    list1.append(string)
list2=[]
no_of_ele_in_list2=int(input("enter number of elements in list 2:"))
for i in range(0,no_of_ele_in_list2):
    string=(input())
    list2.append(string)
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)
