#create a list for storage
num_storage = []

#for-loop to ask for the user 10 input
for num in range(1, 11):
    ask_num = int(input(f"{num}.) Enter num: "))
    num_storage.append(ask_num)

#check if the number has a duplicate
count_dupli = 0
for check in num_storage:
    if check in num_storage:
        count_dupli += 1
    else:
        count_dupli += 0

duplicated_num = []

if count_dupli == 1:
    duplicated_num.append(check)
else:
    pass





