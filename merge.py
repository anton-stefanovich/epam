# функция с использованием методом 'sort()'
def merge_simple(a, b):
    # встроенная склейка
    c = a + b

    # встроенная сортировка
    c.sort()

    return c


# функция без использования метода 'sort()'
def merge_manual(a, b):
    c = list()

    while len(a) and len(b):
        # проверяем последний элемент (индекс '-1'),
        # поскольку метод 'pop()' возвращает именно последний элемент
        c.append(
            (a if a[-1] > b[-1] else b).pop())

    # последовательное применение методов 'pop()' и 'append()' разворачивают массив
    # поэтому разворачиваем его обратно
    c.reverse()

    # одни из массивов пустой, поэтому просто добавляем оставшиеся элементы перед текущим результатом
    c = a + b + c

    return c


a, b = [1, 3, 5], [1, 2, 3, 6]
c = merge_simple(a, b)
c = merge_manual(a, b)