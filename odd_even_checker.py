odd_numbers = []
even_numbers = []

commands = ("exit", "quit")

try:
    while True:
        input_value = input(
            "Enter a number to check whether it is odd or even: ").lower()

        if input_value in commands:
            print("Program exiting... Bye!")
            break

        try:
            number = int(input_value)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if number % 2 == 0:
            print(f"{number} is even!")
            even_numbers.append(number)
        else:
            print(f"{number} is odd!")
            odd_numbers.append(number)

    print(f"Odd numbers checked: {odd_numbers}")
    print(f"Even numbers checked: {even_numbers}")
    print("Goodbye!")

except KeyboardInterrupt:
    print("/nProgram interrupted. Exiting...")
