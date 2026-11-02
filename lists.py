# ===== Методы списка (list) =====
# Список — изменяемая упорядоченная коллекция, допускает повторы.

fruits = ["яблоко", "банан", "вишня"]
print("Исходный список:", fruits)

# append(x) — добавляет один элемент в конец
fruits.append("груша")
print("append('груша'):", fruits)

# extend(iterable) — добавляет все элементы другой коллекции в конец
fruits.extend(["киви", "манго"])
print("extend(['киви', 'манго']):", fruits)

# insert(i, x) — вставляет элемент по индексу
fruits.insert(1, "апельсин")
print("insert(1, 'апельсин'):", fruits)

# remove(x) — удаляет первое вхождение значения (ValueError, если нет)
fruits.remove("банан")
print("remove('банан'):", fruits)

# pop(i) — удаляет и возвращает элемент по индексу (по умолчанию последний)
last = fruits.pop()
print("pop() вернул:", last, "->", fruits)
first = fruits.pop(0)
print("pop(0) вернул:", first, "->", fruits)

# index(x) — индекс первого вхождения
print("index('вишня'):", fruits.index("вишня"))

# count(x) — сколько раз встречается значение
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("\nЧисла:", numbers)
print("count(5):", numbers.count(5))

# sort() — сортирует сам список (на месте), reverse=True — по убыванию
numbers.sort()
print("sort():", numbers)
numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)

# sort(key=...) — сортировка по правилу, например по длине строки
fruits.sort(key=len)
print("fruits.sort(key=len):", fruits)

# reverse() — разворачивает список на месте
numbers.reverse()
print("reverse():", numbers)

# copy() — поверхностная копия (изменения копии не влияют на оригинал)
copy_numbers = numbers.copy()
copy_numbers.append(100)
print("copy() + append(100):", copy_numbers)
print("оригинал не изменился:", numbers)

# clear() — очищает список
copy_numbers.clear()
print("clear():", copy_numbers)
