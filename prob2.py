strings = ['ajlkj;k', 'jfklk', 'fj', 'aa', 'iouijfjdkjl']
sorted_strings = sorted(strings, key= lambda x: (len(x), x))
print(sorted_strings)