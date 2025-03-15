#ask user for input until the value is valid
while True:
    try:
        ask_input = int(input("Enter number(####): "))
    except ValueError:
        print("Value is invalid")
    else:
        # Convert the number to a string
        number_str = str(ask_input)

        # Use a set to track seen digits
        seen_digits = set()
        is_unique = True

        # Iterate over each digit
        for digit in number_str:
            if digit in seen_digits:
                is_unique = False
                break
            seen_digits.add(digit)

        #print statement
        if is_unique:
            print("unique")
        else:
            print("duplicated")

        break