#storage for inputed numbers
num_storage = []
#asks the user for input ten times
for ask_num in range(1, 11):
    ask_for_num = int(input(f"{ask_num}.) Enter number: "))
    num_storage.append(ask_for_num)

#storage for converted numbers
srt_lst = []
#loop that converts every index in num_storage[]
for num in num_storage:
    cnvrt = str(num)
    srt_lst.append(cnvrt)

#to sort all the values from least to greatest
fixed = sorted(srt_lst)
#to find the first index in the list
fisrt_num_in_list = fixed[0]

#print statement
print("the lowest number is: ", fisrt_num_in_list)
