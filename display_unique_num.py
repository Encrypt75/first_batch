#create a list for storage
num_storage = []

#for-loop to ask for the user 10 input
for every_num in range(1, 11):
    ask_num = int(input(f"{every_num}.) Enter num: "))
    num_storage.append(ask_num)

counts = {}  
#check if the number has duplicate
for every_num in num_storage:
    if every_num in counts:
        counts[every_num] += 1  
    else:
        counts[every_num] = 1  

odd = []  # storage for numbers with no duplicates

for number, count in counts.items():
    if count == 1:  # Check if the count is only exactly 1 
        odd.append(number)

#print statement
print(f"Unique numbers: {odd}")