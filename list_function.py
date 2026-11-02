# ===== Мини-функция с методами списка (list) =====
# Функция собирает плейлист: добавляет песни, убирает запрещённые,
# ставит любимую песню первой и сортирует остальные.


def build_playlist(songs: list, new_songs: list, favorite: str, banned: list) -> list:
    """Возвращает готовый плейлист, не меняя исходный список songs.

    songs     — исходный плейлист
    new_songs — песни, которые нужно добавить
    favorite  — любимая песня, она всегда идёт первой
    banned    — песни, которые нужно убрать
    """
    # copy() — работаем с копией, чтобы не испортить исходный список
    playlist = songs.copy()

    # extend() — добавляем все новые песни разом
    playlist.extend(new_songs)

    # remove() — удаляем запрещённые; count() — песня может встречаться несколько раз
    for song in banned:
        while playlist.count(song) > 0:
            playlist.remove(song)

    # Убираем повторы: append() кладём песню, только если её ещё нет
    unique = []
    for song in playlist:
        if song not in unique:
            unique.append(song)
    playlist = unique

    # index() + pop() — достаём любимую песню с её места
    if favorite in playlist:
        playlist.pop(playlist.index(favorite))

    # sort(key=...) — остальные песни по алфавиту без учёта регистра
    playlist.sort(key=str.lower)

    # insert(0, ...) — любимая песня встаёт первой
    playlist.insert(0, favorite)
    return playlist


def shuffle_backwards(playlist: list) -> list:
    """Возвращает плейлист в обратном порядке (для режима «с конца»)."""
    # copy() + reverse() — reverse меняет список на месте, поэтому сначала копия
    result = playlist.copy()
    result.reverse()
    return result


if __name__ == "__main__":
    my_songs = ["Rammstein - Sonne", "Imagine Dragons - Believer", "Баста - Сансара"]
    playlist = build_playlist(
        songs=my_songs,
        new_songs=["Queen - Bohemian Rhapsody", "Баста - Сансара", "Плохая песня"],
        favorite="Queen - Bohemian Rhapsody",
        banned=["Плохая песня"],
    )

    print("Плейлист:")
    for number, song in enumerate(playlist, start=1):
        print(f"  {number}. {song}")

    print("\nС конца:", shuffle_backwards(playlist))
    print("Исходный список не изменился:", my_songs)

    # clear() — очистить плейлист
    playlist.clear()
    print("После clear():", playlist)
