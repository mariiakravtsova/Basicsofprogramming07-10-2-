# Стан води за температурою
temperature = int(input("Введіть температуру води в °C: "))

if temperature <= 0:
    print("Лід")
elif temperature < 100:
    print("Вода")
else:
    print("Пара")

# Пора доби за годиною

hour = int(input("Введіть годину від 0 до 23: "))

if hour <= 5:
    print("Ніч")
elif hour <= 11:
    print("Ранок")
elif hour <= 17:
    print("День")
else:
    print("Вечір")