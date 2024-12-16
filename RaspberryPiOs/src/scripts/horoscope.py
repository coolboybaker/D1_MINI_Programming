import random

zodiac_signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
predictions = [
    "сегодня ждет удачный день",
    "возможны неожиданные перемены",
    "стоит обратить внимание на свое здоровье",
    "вас ждет приятный сюрприз",
    "лучше воздержаться от важных решений",
    "благоприятное время для новых начинаний",
    "возможны финансовые поступления",
    "стоит уделить время близким",
    "ожидается интересное знакомство",
    "хороший день для творчества"
]
advice = [
    "Будьте внимательны к мелочам",
    "Доверьтесь своей интуиции",
    "Не бойтесь рисковать",
    "Проявите терпение",
    "Будьте открыты новому",
    "Сконцентрируйтесь на главном",
    "Не забывайте об отдыхе",
    "Прислушайтесь к советам друзей",
    "Действуйте решительно",
    "Будьте гибкими в планах"
]

def generate_horoscope():
    sign = random.choice(zodiac_signs)
    prediction = random.choice(predictions)
    today_advice = random.choice(advice)
    
    horoscope = f"Гороскоп для {sign}: {prediction}. Совет дня: {today_advice}."
    return horoscope

print(generate_horoscope())

print("\nГороскоп для всех знаков зодиака:")
for sign in zodiac_signs:
    prediction = random.choice(predictions)
    today_advice = random.choice(advice)
    print(f"{sign}: {prediction} {today_advice}")
