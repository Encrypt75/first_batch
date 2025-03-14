#storage for inputed numbers
num_storage = []
#for-loop for asking
for ask_num in range(1, 11):
    ask_for_num = int(input(f"{ask_num}.) Enter number: "))
    num_storage.append(ask_for_num)


#to sort all the values from least to greatest
srt_lst = sorted(num_storage)

#print statement
print(srt_lst)

