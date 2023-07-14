def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to the bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # it only allows the whole numbers
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number.")

    return lines