# Данные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка, высчитывающая разницу длин строк из списков first и second
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка, сравнивающая длины строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))
print(list(second_result))