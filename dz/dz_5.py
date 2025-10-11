result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a менше, ніж b — ValueError")
        if b > 100:
            raise IndexError("b більше 100 — IndexError")
        return a / b
    except ZeroDivisionError:
        print(f"Помилка: ділення на нуль (a={a}, b={b})")
    except TypeError:
        print(f"Помилка: невірний тип даних (a={a}, b={b})")
    except ValueError as e:
        print(f"Помилка: {e}")
    except IndexError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Невідомий виняток: {type(e).__name__} — {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, 0: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Помилка при обробці ключа {key}: {e}")

print("\nРезультат:", result)
