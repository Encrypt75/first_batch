#initialization
even_cntr = 0

#ask for input and verifies if the input is even or not
for minus_total in range(1, 11):
    ask =  float(input(f"Input num{minus_total}: "))
    if ask % 2 == 0:
        even_cntr += 1

#print statement
print(f"total of even numbers: {even_cntr}")