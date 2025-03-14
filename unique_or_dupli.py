#storage for entered number
entered_number = set()

#check if the value is valid
while True:
    try:
        #the user must input numbers
        ask = int(input("Enter number(####): "))
    except ValueError:
        print("Value is invalid")
    else:
        if ask in entered_number:
            print("duplicated")
        else:
            print("unique")
            entered_number.add(ask)