#create a dictionary {key: value}
dict1 = {1: 2, 3: 6}
#convert dictionary to string
#create a iteration the checks every key and value
#create num_list and count_list
#key will append the num_list
#value will append to count_list
num_list = []
count_list = []

for key, count in dict1:
    num_list.append(key)
    count_list.append(count)

print(num_list, count_list)
