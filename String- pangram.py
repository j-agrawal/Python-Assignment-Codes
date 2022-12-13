inp_string= input("enter a string:")
string2="abcdefghijklmnopqurstuvwxyz"
for i in string2:
    if i not in inp_string:
        print(i,end="")
