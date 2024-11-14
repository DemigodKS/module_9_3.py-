first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))
#1 вариант
second_result = (len(first[i])==len(second[i]) for i in range(len(first)))
print(list(second_result))
#2 вариант
second_result = (len(first[x])==len(second[y]) for x, y in zip(range(len(first)),range(len(second))))
print(list(second_result))
