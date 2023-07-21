numbers = [1, 2, 4, 5, 7]

count = sum(1 for i in numbers if i % 2 == 0)
print(count)

count = sum(i % 2 == 0 for i in numbers)
print(count)
