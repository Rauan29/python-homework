# ===== Методы словаря (dict) =====
# Словарь — коллекция пар «ключ: значение», ключи уникальны.

student = {"name": "Рауан", "age": 17, "city": "Алматы"}
print("Исходный словарь:", student)

# get(key, default) — безопасно получить значение (без KeyError)
print("\nget('name'):", student.get("name"))
print("get('email', 'нет почты'):", student.get("email", "нет почты"))

# keys(), values(), items() — ключи, значения и пары
print("keys():", list(student.keys()))
print("values():", list(student.values()))
print("items():", list(student.items()))

for key, value in student.items():
    print(f"  {key} -> {value}")

# update(other) — добавить/обновить сразу несколько пар
student.update({"age": 18, "course": "Python Middle"})
print("\nupdate({'age': 18, 'course': ...}):", student)

# setdefault(key, default) — вернуть значение; если ключа нет — создать его
student.setdefault("grades", [])
student["grades"].append(5)
print("setdefault('grades', []):", student)

# pop(key, default) — удалить ключ и вернуть значение
city = student.pop("city")
print("\npop('city') вернул:", city, "->", student)
print("pop('phone', None):", student.pop("phone", None))

# popitem() — удалить и вернуть последнюю добавленную пару
print("popitem():", student.popitem(), "->", student)

# fromkeys(keys, value) — создать словарь из списка ключей
subjects = ["математика", "физика", "информатика"]
journal = dict.fromkeys(subjects, 0)
print("\ndict.fromkeys(subjects, 0):", journal)

# copy() — поверхностная копия
journal_copy = journal.copy()
journal_copy["математика"] = 5
print("copy() изменили копию:", journal_copy)
print("оригинал:", journal)

# Практический пример: подсчёт слов
text = "кот пёс кот рыба пёс кот"
counter = {}
for word in text.split():
    counter[word] = counter.get(word, 0) + 1
print("\nПодсчёт слов:", counter)

# clear() — очистить словарь
journal.clear()
print("clear():", journal)
