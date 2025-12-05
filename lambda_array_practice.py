"""
Question
Write a Python programme called 'lambda_array_practice.py' that works with a list of
whole numbers and uses lambda functions in at least three different ways.

Your programme should
1.	Ask the user to enter several whole numbers separated by spaces, then store these
values in a list of integers
2.	Use a lambda function with map to create a new list that contains the square of
each number
3.	Use a lambda function with filter to create a list that contains only the even
numbers
4.	Use a lambda function as the key argument of sorted to produce a list of the
original numbers sorted by their absolute value
5.	Print all of the following with clear labels
        the original list
        the list of squares
        the list of even numbers
        the list sorted by absolute value
Your code should be neatly formatted and should include at least one short comment
that explains what each lambda expression is doing.
"""

# Ask the user for input and convert it to a list of integers
user_input = input("Enter whole numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Use lambda with map to create a list of squares
squares = list(map(lambda x: x * x, numbers))

# Use lambda with filter to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use lambda as the key for sorted to sort by absolute value
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))

# Print all results with clear labels
print("Original numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Sorted by absolute value:", sorted_by_abs)
