import random

class Human:
    def __init__(self, name):
        self.name = name


class FootballPlayer(Human):
    def __init__(self, name):
        super().__init__(name)
        self.team = None


names = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار",
         "میلاد", "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی",
         "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

# ساخت بازیکنان
players = [FootballPlayer(name) for name in names]

# تصادفی‌سازی
random.shuffle(players)

# تقسیم به دو تیم
for i, player in enumerate(players):
    if i < 11:
        player.team = "A"
    else:
        player.team = "B"

# چاپ خروجی
for player in players:
    print(f"نام بازیکن: {player.name} - تیم: {player.team}")