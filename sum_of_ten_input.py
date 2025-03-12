#input ten numbers using for loop
total = 0
for ask in range(1, 11):
    num = int(input("Enter a number: "))
    total += num

#prints the sum of the 10 numbers
print(f"total: {total}")