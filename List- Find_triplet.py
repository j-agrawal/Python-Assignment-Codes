list1=[]
no_of_ele_in_list1=int(input("enter number of elements in list 1:"))
for i in range(0,no_of_ele_in_list1):
    element=int(input())
    list1.append(element)
sum=int(input("enter the value of sum:"))
list2=[]
for i in range(0,len(list1)):
    for j in range (i+1,len(list1)):
        for k in range (j+1,len(list1)):
            if (list1[i]+list1[j]+list1[k]==sum):
                list2.append(list1[i])
                list2.append(list1[j])
                list2.append(list1[k])
print(list2)
