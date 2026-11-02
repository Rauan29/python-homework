# ===== Мини-функция с методами строк (str) =====
# Функция «нормализует» анкету пользователя, введённую как попало.


def format_profile(raw_name: str, raw_email: str, raw_phone: str, raw_bio: str) -> str:
    """Принимает «грязные» данные анкеты и возвращает аккуратную карточку профиля.

    raw_name  — имя с лишними пробелами и в любом регистре
    raw_email — почта с пробелами и заглавными буквами
    raw_phone — телефон в любом формате: 8 (701) 123-45-67, +7 701 1234567 и т.д.
    raw_bio   — текст «о себе» с лишними пробелами
    """
    # strip() — убрать пробелы по краям; split() + join() — убрать лишние пробелы внутри
    # title() — каждое слово с заглавной буквы
    name = " ".join(raw_name.strip().split()).title()

    # lower() — email всегда в нижнем регистре
    email = raw_email.strip().lower()
    # count() / find() / endswith() — простая проверка email
    if email.count("@") != 1 or email.find(".", email.find("@")) == -1 or email.endswith("."):
        email_status = "некорректный"
    else:
        email_status = "ок"

    # replace() — убрать лишние символы; isdigit() — проверить, что остались только цифры
    phone = raw_phone
    for symbol in " -()+":
        phone = phone.replace(symbol, "")
    # startswith() — заменить ведущую 8 на 7 (формат KZ/RU)
    if phone.startswith("8") and len(phone) == 11:
        phone = "7" + phone[1:]
    if phone.isdigit() and len(phone) == 11:
        phone = f"+{phone[0]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:]}"
    else:
        phone = "некорректный номер"

    # capitalize() — первая буква заглавная; обрезаем длинное описание
    bio = " ".join(raw_bio.split()).capitalize()
    if len(bio) > 40:
        bio = bio[:40].rstrip() + "..."

    # center() и ljust() — красивое оформление «карточки»
    width = 46
    lines = [
        " ПРОФИЛЬ ".center(width, "="),
        f"Имя:     {name}".ljust(width),
        f"Email:   {email} ({email_status})".ljust(width),
        f"Телефон: {phone}".ljust(width),
        f"О себе:  {bio}".ljust(width),
        "=" * width,
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(format_profile(
        raw_name="   рауАН    абишев  ",
        raw_email="  Rauan.Abishev@GMAIL.com ",
        raw_phone="8 (701) 123-45-67",
        raw_bio="   изучаю   python   и   django,   делаю   сайт   для   стоматологии  ",
    ))
    print()
    print(format_profile("иван", "ivan@@mail", "12345", "привет"))
