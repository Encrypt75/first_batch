#initialization
total = 0
#ask for first input
first_num = float(input("Input num1: "))

#ask for the other 9 input using for-loop
for minus_total in range(2, 11):
    ask =  float(input(f"Input num{minus_total}: "))
    #increment
    total += ask

#print statement where the first is being subtracted to the remaining numbers
print(f"{first_num} - {total} = {first_num - total}")