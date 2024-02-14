list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]

intersection = filter(lambda x: x in list2, list1)

print(list(intersection))