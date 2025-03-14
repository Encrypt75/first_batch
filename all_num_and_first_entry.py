#list for storage
num_storage = []

#ask user 10 input 
for num in range(1, 11):
    ask_num = int(input(f"{num}.) Enter num: "))
    num_storage.append(ask_num)

#convert list to set
cnvrt_lst = set(num_storage)
#print and convert set back to list
print(list(cnvrt_lst))