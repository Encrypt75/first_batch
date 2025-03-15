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
    number = is_valid(f"{ask_num}.) Enter number: ")
    num_storage.append(number)

#storage for converted numbers
srt_lst = []
#loop that converts every index in num_storage[]
for num in num_storage:
    cnvrt = str(num)
    srt_lst.append(cnvrt)

#to sort all the values from least to greatest
srt_lst = sorted(srt_lst)
#finds the value of the fisrt index
last_num_in_list = srt_lst[-1]

#print statement
print("the highest number is: ", last_num_in_list)