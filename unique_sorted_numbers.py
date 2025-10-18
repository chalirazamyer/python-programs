"""
Question:

Write a program to first count total numbers count in a list,
sort it and then remove any duplicates.
"""


# First define a list with numbers
numbers = [5, 2, 1, 7, -1, -1, 2, 1, 42, 12, 3423, 11, -10, 7, 1, 3, 0, 4]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)  # [0, 1, 1, 2, 3, 4, 5, 7, 7]

counts = 0
for _ in numbers:
    counts += 1

for item in range(counts):
    for number in numbers:
        if number>numbers[item]:
            largest = number
            largest_index = numbers.index(largest)
            temp = numbers[item]
            numbers[item] = numbers[largest_index]
            numbers[largest_index] = temp
print(numbers)

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


"""
Swap logic recap, why one version fails,
and the others work 

The following broken swap duplicates a value;
it does not exchange 

numbers[i] = numbers[j]
numbers[j] = numbers[i]

Step by step with numbers[i] = 5, numbers[j] = 2
1) After the first line, both positions contain 2
2) The second line reads numbers[i], which is already 2,
then writes 2 back to numbers[j]

The original 5 is lost; no real swap happened. 


Correct swap using a temporary variable

tmp = numbers[i]
numbers[i] = numbers[j]
numbers[j] = tmp

Why this works
You preserve the original numbers[i] in tmp,
after you copy numbers[j] into numbers[i]
You still have the saved value to place into numbers[j] 


OR


Python tuple swap, concise and safe

numbers[i], numbers[j] = numbers[j], numbers[i]

Why this works
Python evaluates the right side first, and it builds
the pair (numbers[j], numbers[i]) using the original
values 

Then, it assigns both results to the left side in one
step; no value is lost. 

Tiny trace to visualise 
Start list [5, 2, 1], comparing i = 0, j = 1
Broken swap gives [2, 2, 1]
Temp swap gives [2, 5, 1]
Tuple swap gives [2, 5, 1]

Takeaway: never overwrite a value you still need;
keep it in a temporary variable. 

Or let Python do it with tuple unpacking. 
"""
