inp_string= input("enter the input string:")
dict={}
for i in inp_string:
    dict[i]=None
for i in range (0,len(inp_string)):
    a=1
    if dict[inp_string[i]]==None:
        for j in range(i+1,len(inp_string)):
            if inp_string[i]==inp_string[j]:
                a+=1
        dict[inp_string[i]]=a
print(dict)
