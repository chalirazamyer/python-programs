
factorial = int(input("Give the number for factorial: "))

output = z = multiply = factorial

for j in range(factorial):
    multiply = multiply - 1
    if multiply != 0:
        output = z * multiply
        print(f"Iterative wise output {z} * {multiply}: {output}")
        z = output

print(f"Factorial of {factorial} is: {output}")