numbers = [1, 2, 3, 4]
max_of_2 = lambda x, y: x if x > y else y

def find_max(numbers, function):
    max_num = numbers[0]
    for element in numbers:
        max_num = max_of_2(max_num, element)
    return max_num

print(find_max(numbers, max_of_2))