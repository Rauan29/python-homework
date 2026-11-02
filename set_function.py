# ===== Мини-функция с методами множества (set) =====
# Функция сравнивает друзей двух людей, как в соцсети:
# общие друзья, рекомендации «возможно, вы знакомы» и т.д.


def compare_friends(my_friends: list, his_friends: list, blocked: list) -> dict:
    """Возвращает словарь с результатами сравнения двух списков друзей.

    my_friends  — мои друзья (могут быть повторы)
    his_friends — друзья другого человека
    blocked     — люди, которых я заблокировал, их не рекомендуем
    """
    # set() — превращаем списки во множества, повторы исчезают сами
    mine = set(my_friends)
    his = set(his_friends)

    # intersection() — общие друзья
    common = mine.intersection(his)

    # difference() — его друзья, которых нет у меня, это рекомендации
    recommended = his.difference(mine)

    # discard() — убираем заблокированных; discard не падает, если человека там нет
    for person in blocked:
        recommended.discard(person)

    # union() — все люди из обоих списков
    everyone = mine.union(his)

    # symmetric_difference() — друзья только одного из нас
    only_one = mine.symmetric_difference(his)

    # isdisjoint() — True, если общих друзей нет совсем
    # issubset() — True, если все мои друзья есть и у него
    return {
        "общие": common,
        "рекомендации": recommended,
        "все": everyone,
        "только у одного": only_one,
        "нет общих": mine.isdisjoint(his),
        "мои друзья входят в его": mine.issubset(his),
    }


def add_friends(friends: set, *new_people: str) -> set:
    """Добавляет новых друзей и возвращает новое множество (исходное не меняется)."""
    # copy() — копия; add() — добавить по одному (повтор просто игнорируется)
    result = friends.copy()
    for person in new_people:
        result.add(person)
    return result


if __name__ == "__main__":
    report = compare_friends(
        my_friends=["Аня", "Боря", "Вика", "Аня"],
        his_friends=["Вика", "Гена", "Дима", "Ева"],
        blocked=["Дима"],
    )
    for key, value in report.items():
        print(f"{key}: {value}")

    friends = {"Аня", "Боря"}
    print("\nadd_friends:", add_friends(friends, "Вика", "Аня"))
    print("Исходное множество не изменилось:", friends)
