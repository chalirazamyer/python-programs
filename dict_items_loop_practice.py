
"""
Question:

Write a Python script that defines a dictionary named point with the keys x and y.
Then use a for loop over point.items() to print each key and its value, in order
to practise iterating through dictionaries in Python.
"""


point = dict(x=1, y=2)

for key, value in point.items():
    print(f"Key: {key}, Value: {value}")
