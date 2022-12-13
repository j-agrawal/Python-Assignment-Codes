list1=[]
no_of_ele_in_list1=int(input("enter number of elements in list 1:"))
for i in range(0,no_of_ele_in_list1):
    element=int(input())
    list1.append(element)
print("positive numbers are:")
for i in list1:
    if i >= 0:
        print(i)
