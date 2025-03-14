num_storage = []
for ask_num in range(1, 11):
    ask_for_num = int(input(f"{ask_num}.) Enter number:"))
    num_storage.append(ask_for_num)

srt_lst = []
for num in num_storage:
    cnvrt = str(num)
    srt_lst.append(cnvrt)

fixed = sorted(srt_lst)
fisrt_num_in_list = fixed[0]

print("the lowest number is: ", fisrt_num_in_list)
