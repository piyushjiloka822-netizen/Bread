def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

# Using it to print even numbers up to 10
for num in even_numbers(10):
    print(num)