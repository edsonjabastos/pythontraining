accumulator = 0
for number in range(1, 101):
    if number % 2 == 0:
        accumulator += number
        # print(number)
        # print(accumulator)
print(accumulator)

# teacher solution

total = 0
for number in range(2, 101, 2):
    total += number
print(total)