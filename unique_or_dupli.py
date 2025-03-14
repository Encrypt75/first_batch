def has_duplicate_digits(number):
    str_number = str(number)
    seen_digits = set()
    for digit in str_number:
        if digit in seen_digits:
            return True
        seen_digits.add(digit)
    return False

def main():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            if has_duplicate_digits(number):
                print("Duplicate")
            else:
                print("Unique")
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

main()
