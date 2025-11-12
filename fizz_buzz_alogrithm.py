

def fizz_buzz(input_value):
    if (input_value % 3 == 0) and (input_value % 5 == 0):
        return "FizzBuzz"
    if input_value % 3 == 0:
        return "Fizz"
    if input_value % 5 == 0:
        return "Buzz"
    return input_value


print(fizz_buzz(3))  # output: Fizz
print(fizz_buzz(5))  # output: Buzz
print(fizz_buzz(7))  # output: 7
print(fizz_buzz(15))  # output: FizzBuzz
