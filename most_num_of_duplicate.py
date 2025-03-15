#def that checks if the input is valid
def invalid(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Try again.")

#def that checks the number of the largest duplicate
def most_num_of_dupli(list_store):
    if not list_store:
        return None
    return max(set(list_store), key=list_store.count)

list_store = []

#ask user 10 times for input
for ask in range(1, 11):
    number = invalid(f"{ask}.) Enter number: ")
    list_store.append(number)

result = most_num_of_dupli(list_store)

#print statement
print(f"The number with the most duplicates is: {result}")