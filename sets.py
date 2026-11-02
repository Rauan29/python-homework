# ===== Методы множества (set) =====
# Множество — неупорядоченная коллекция уникальных элементов.

python_students = {"Аня", "Боря", "Вика", "Гена"}
js_students = {"Вика", "Гена", "Дима", "Ева"}
print("Python:", python_students)
print("JS:", js_students)

# add(x) — добавляет элемент (дубликат просто игнорируется)
python_students.add("Жора")
python_students.add("Аня")
print("\nadd('Жора'), add('Аня'):", python_students)

# update(iterable) — добавляет сразу несколько элементов
python_students.update(["Зоя", "Илья"])
print("update(['Зоя', 'Илья']):", python_students)

# remove(x) — удаляет элемент (KeyError, если его нет)
python_students.remove("Илья")
print("remove('Илья'):", python_students)

# discard(x) — удаляет элемент, но без ошибки, если его нет
python_students.discard("Несуществующий")
print("discard('Несуществующий') — ошибки нет")

# pop() — удаляет и возвращает произвольный элемент
removed = python_students.pop()
print("pop() вернул:", removed)

# Восстановим набор для операций над множествами
python_students = {"Аня", "Боря", "Вика", "Гена"}

# union(other) / | — объединение: все ученики
print("\nunion (все):", python_students.union(js_students))

# intersection(other) / & — пересечение: учат оба языка
print("intersection (оба языка):", python_students.intersection(js_students))

# difference(other) / - — разность: только Python
print("difference (только Python):", python_students.difference(js_students))

# symmetric_difference(other) / ^ — только один из языков
print("symmetric_difference (ровно один язык):",
      python_students.symmetric_difference(js_students))

# issubset / issuperset / isdisjoint — проверки отношений
small = {"Вика", "Гена"}
print("\n{'Вика', 'Гена'}.issubset(python):", small.issubset(python_students))
print("python.issuperset({'Вика', 'Гена'}):", python_students.issuperset(small))
print("python.isdisjoint({'Яна'}):", python_students.isdisjoint({"Яна"}))

# Практический пример: убрать дубликаты из списка
emails = ["a@mail.ru", "b@mail.ru", "a@mail.ru", "c@mail.ru", "b@mail.ru"]
print("\nУникальные email:", set(emails))

# copy() и clear()
backup = python_students.copy()
python_students.clear()
print("После clear():", python_students, "| копия:", backup)
