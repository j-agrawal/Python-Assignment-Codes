inp_string= input("enter a string:")
count=0
for i in range (0,len(inp_string)):
    for j in range(i,len(inp_string)):
        count+=1
print(count)
