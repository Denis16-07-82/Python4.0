# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Список: {lst}")

new_st = set(lst)
new_lst = list(new_st)
[lst.remove(i) for i in new_lst ]
new_st1 = set(lst)
print(f"Список из неповторяющихся элементов: {list(new_st.difference(new_st1))}")