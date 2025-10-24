

# defining a prime number list:
numbers = []

for i in range(2, 100):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        numbers.append(i)

print(numbers)
