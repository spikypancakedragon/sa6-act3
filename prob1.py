number = 25
sum_of_digits = lambda x: sum(int(digit) for digit in str(x))
print(sum_of_digits(number))