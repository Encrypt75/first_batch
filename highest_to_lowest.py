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

#to sort all the values from least to greatest
srt_lst = sorted(num_storage)

#print statement, and reverse the values of the list
print(srt_lst[::-1])