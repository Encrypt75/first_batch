#print numbers from 0 to 100 except number ending with 0 (using for loop)
for cnt in range(0, 101):
    cnrt_str = str(cnt) #convert string
    if cnrt_str.find("0") == True: #convert string
        continue
    elif cnt == 0:
        continue
    else:
        print(int(cnt)) #convert string back to an integer
print("==End==")