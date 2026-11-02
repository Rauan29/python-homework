# ===== Мини-функция с методами словаря (dict) =====
# Функция считает корзину интернет-магазина: сколько каких товаров,
# сумма по каждому товару и итог со скидкой.

PRICES = {"хлеб": 250, "молоко": 450, "сыр": 1800, "яблоки": 900}


def make_cart(items: list) -> dict:
    """Собирает корзину из списка покупок: {товар: количество}."""
    cart = {}
    for item in items:
        # get(item, 0) — если товара ещё нет, считаем, что его 0 штук
        cart[item] = cart.get(item, 0) + 1
    return cart


def cart_total(cart: dict, prices: dict, discount_codes: dict, code: str = "") -> dict:
    """Возвращает чек: сумма по товарам, скидка и итог.

    cart           — корзина {товар: количество}
    prices         — цены {товар: цена}
    discount_codes — промокоды {код: скидка в процентах}
    code           — введённый промокод
    """
    # fromkeys() — заготовка чека: каждому товару сумма 0
    receipt = dict.fromkeys(cart.keys(), 0)
    unknown = []

    # items() — перебираем пары «товар — количество»
    for item, count in cart.items():
        price = prices.get(item)
        if price is None:
            unknown.append(item)
            # pop() — убираем из чека товар, которого нет в прайсе
            receipt.pop(item)
            continue
        receipt[item] = price * count

    # values() — складываем суммы всех товаров
    subtotal = sum(receipt.values())

    # get(code, 0) — неверный промокод означает 0% скидки
    percent = discount_codes.get(code.strip().upper(), 0)
    discount = subtotal * percent // 100

    # update() — дописываем итоговые строки в чек
    receipt.update({"скидка": -discount, "итого": subtotal - discount})

    # setdefault() — список неизвестных товаров есть в чеке всегда, даже пустой
    receipt.setdefault("нет в продаже", unknown)
    return receipt


if __name__ == "__main__":
    cart = make_cart(["хлеб", "молоко", "хлеб", "сыр", "арбуз"])
    print("Корзина:", cart)

    receipt = cart_total(cart, PRICES, {"SALE10": 10, "VIP": 25}, code=" sale10 ")
    print("\nЧек:")
    for line, value in receipt.items():
        print(f"  {line}: {value}")

    # popitem() — достаём последнюю пару; keys() — какие строки есть в чеке
    print("\npopitem():", receipt.popitem())
    print("Строки чека:", list(receipt.keys()))

    # copy() и clear() — копию оставили, корзину очистили
    old_cart = cart.copy()
    cart.clear()
    print("\nКорзина после clear():", cart, "| копия:", old_cart)
