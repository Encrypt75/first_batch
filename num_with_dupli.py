#storage of inputs
num_storage = []

#ask user for an input
for every_num in range(1, 11):
    ask_num = int(input(f"{every_num}.) Enter number: "))
    num_storage.append(ask_num)

counts = {}

#counts the number of repeated numbers
for every_num in num_storage:
    if every_num in counts:
        counts[every_num] += 1  
    else:
        counts[every_num] = 1 

#storing of duplicated numbers
duplicate_num = []

#checks if count is greater 1 or not
for number, count in counts.items():
    if count != 1:
        duplicate_num.append(number)

#print and calls duplicate_num
print(f"numbers with duplicates: {duplicate_num}")