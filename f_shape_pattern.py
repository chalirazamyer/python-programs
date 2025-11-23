"""
Questions:

xxxxx
xx
xxxxx
xx
xx

Using nested loops, draw the f shape, as shown above.
Hint!  You can use the list, numbers = [5, 2, 5, 2, 2]
These values in the list determine the number of x's we have in each
line. For example, the first item in this list shows that we should
have 5 x's on the first line. On the second line we're going to have
2 x's, on the third line we're going to have 5 x's, on the fourth and
fifth we are going to have 2 x's. Here is another tip, Using your for
loop you need to iterate over this list. In each iteration you get one
number, this determines the number of x's to be displayed on that
particular line. Don't cheat by multiplying the list with x to print
the shape. Imagine in Python, we cannot multiply a string by a number.
To solve this problem, use nested loop.
"""

numbers = [5, 2, 5, 1, 2, 2]


for number in numbers:
    output = ""
    for print_asterisk in range(number):
        output += "*"
    print(output)
