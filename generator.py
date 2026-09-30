def countdown(n):
    while n >= 1:
        yield n
        n -= 1

# Using a loop to print all the numbers
for number in countdown(5):
    print(number)