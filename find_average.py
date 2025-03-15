#try again until the value is valid
def is_valid(number):
    while True:
        try:
            num = int(input(number))
            return num
        except ValueError:
            print("Invalid input, try again.")

#storage for inputed numbers
num_storage = []
#for-loop for asking
for ask_num in range(1, 11):
    numbers = is_valid(f"{ask_num}.) Enter number: ")
    num_storage.append(numbers)

#initialize
total = 0
#for-loop to check for every values in a loop
for num in num_storage:
    total += num

#print statement
print(f"{total} / 10 = {total/10}")
