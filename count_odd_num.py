#input ten numbers using for loop
odd_total = 0
for ask in range(1, 11):
    num = int(input("Enter a number: "))

    if num % 2 != 0:
        odd_total += 1

#prints only the ODD numbers
print(f"total of odd numbers: {odd_total}")