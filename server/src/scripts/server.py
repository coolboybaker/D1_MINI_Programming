from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse
import datetime
import random
import math
from collections import defaultdict
from typing import List, Tuple, Dict

class CelestialBody:
    def __init__(self, name: str, symbol: str, degrees: float):
        self.name = name
        self.symbol = symbol
        self.degrees = degrees

class ZodiacSign:
    def __init__(self, name: str, symbol: str, start_date: Tuple[int, int], end_date: Tuple[int, int], 
                 element: str, quality: str, ruling_planet: str):
        self.name = name
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.element = element
        self.quality = quality
        self.ruling_planet = ruling_planet

class AstrologicalChart:
    def __init__(self, zodiac_sign: ZodiacSign, ascendant: ZodiacSign, moon_sign: ZodiacSign):
        self.zodiac_sign = zodiac_sign
        self.ascendant = ascendant
        self.moon_sign = moon_sign
        self.planets = self._generate_planet_positions()

    def _generate_planet_positions(self) -> List[CelestialBody]:
        planets = [
            ("Солнце", "☉"), ("Луна", "☽"), ("Меркурий", "☿"), ("Венера", "♀"), ("Марс", "♂"),
            ("Юпитер", "♃"), ("Сатурн", "♄"), ("Уран", "♅"), ("Нептун", "♆"), ("Плутон", "♇")
        ]
        return [CelestialBody(name, symbol, random.uniform(0, 360)) for name, symbol in planets]

class HoroscopeGenerator:
    def __init__(self):
        self.zodiac_signs = self._initialize_zodiac_signs()
        self.aspects = ["Любовь", "Карьера", "Здоровье", "Финансы", "Личностный рост", "Учеба", "Хобби"]
        self.predictions = self._load_predictions()
        self.colors = {
            "Овен": "красный", "Телец": "зеленый", "Близнецы": "желтый", "Рак": "серебряный",
            "Лев": "золотой", "Дева": "коричневый", "Весы": "розовый", "Скорпион": "темно-красный",
            "Стрелец": "фиолетовый", "Козерог": "черный", "Водолей": "синий", "Рыбы": "бирюзовый"
        }

    def _initialize_zodiac_signs(self) -> List[ZodiacSign]:
        return [
            ZodiacSign("Овен", "♈", (3, 21), (4, 19), "Огонь", "Кардинальный", "Марс"),
            ZodiacSign("Телец", "♉", (4, 20), (5, 20), "Земля", "Фиксированный", "Венера"),
            ZodiacSign("Близнецы", "♊", (5, 21), (6, 20), "Воздух", "Мутабельный", "Меркурий"),
            ZodiacSign("Рак", "♋", (6, 21), (7, 22), "Вода", "Кардинальный", "Луна"),
            ZodiacSign("Лев", "♌", (7, 23), (8, 22), "Огонь", "Фиксированный", "Солнце"),
            ZodiacSign("Дева", "♍", (8, 23), (9, 22), "Земля", "Мутабельный", "Меркурий"),
            ZodiacSign("Весы", "♎", (9, 23), (10, 22), "Воздух", "Кардинальный", "Венера"),
            ZodiacSign("Скорпион", "♏", (10, 23), (11, 21), "Вода", "Фиксированный", "Плутон"),
            ZodiacSign("Стрелец", "♐", (11, 22), (12, 21), "Огонь", "Мутабельный", "Юпитер"),
            ZodiacSign("Козерог", "♑", (12, 22), (1, 19), "Земля", "Кардинальный", "Сатурн"),
            ZodiacSign("Водолей", "♒", (1, 20), (2, 18), "Воздух", "Фиксированный", "Уран"),
            ZodiacSign("Рыбы", "♓", (2, 19), (3, 20), "Вода", "Мутабельный", "Нептун")
        ]

    def _load_predictions(self) -> Dict[str, Dict[str, List[str]]]:
        predictions = defaultdict(lambda: defaultdict(list))
        for sign in self.zodiac_signs:
            predictions[sign.name]["Любовь"] = [
                f"Влияние {sign.ruling_planet}а усилит вашу харизму и привлекательность.",
                f"Энергия {sign.element}а поможет вам найти гармонию в отношениях.",
                f"Ваше {sign.quality.lower()} качество привлечет к вам интересных людей.",
                f"Сегодня {sign.name} может ожидать неожиданных романтических встреч.",
                f"Звезды советуют {sign.name} быть более открытым и искренним в любви.",
                f"Благоприятный день для укрепления существующих отношений.",
                f"Возможно, стоит пересмотреть свои ожидания от партнера.",
                f"Ваша интуиция в любовных делах сегодня особенно сильна.",
                f"Не бойтесь проявлять инициативу в романтических отношениях.",
                f"Сегодня хороший день для примирения и восстановления связей."
            ]
            predictions[sign.name]["Карьера"] = [
                f"Влияние {sign.ruling_planet}а усилит ваши лидерские качества.",
                f"Энергия {sign.element}а поможет вам преодолеть трудности на работе.",
                f"Ваше {sign.quality.lower()} качество будет высоко оценено коллегами.",
                f"Сегодня {sign.name} может ожидать неожиданных карьерных возможностей.",
                f"Звезды советуют {sign.name} быть более инициативным в профессиональной сфере.",
                f"Хороший день для начала нового проекта или презентации идей.",
                f"Возможно, пришло время задуматься о смене работы или повышении квалификации.",
                f"Ваши творческие способности сегодня могут принести неожиданные результаты.",
                f"Не бойтесь брать на себя ответственность за важные решения.",
                f"Сегодня благоприятный день для налаживания деловых связей."
            ]
            predictions[sign.name]["Здоровье"] = [
                f"Влияние {sign.ruling_planet}а усилит вашу жизненную энергию.",
                f"Энергия {sign.element}а поможет вам восстановить силы и здоровье.",
                f"Ваше {sign.quality.lower()} качество поможет преодолеть любые недомогания.",
                f"Сегодня {sign.name} может ощутить прилив сил и бодрости.",
                f"Звезды советуют {sign.name} уделить особое внимание своему здоровью.",
                f"Хороший день для начала новой программы упражнений или диеты.",
                f"Возможно, стоит пересмотреть свой режим сна и отдыха.",
                f"Ваше эмоциональное состояние сегодня напрямую влияет на физическое здоровье.",
                f"Не игнорируйте сигналы своего тела, прислушивайтесь к нему.",
                f"Сегодня благоприятный день для медитации и релаксации."
            ]
            predictions[sign.name]["Финансы"] = [
                f"Влияние {sign.ruling_planet}а может принести неожиданную финансовую удачу.",
                f"Энергия {sign.element}а поможет вам найти новые источники дохода.",
                f"Ваше {sign.quality.lower()} качество поможет в финансовых переговорах.",
                f"Сегодня {sign.name} может ожидать неожиданных денежных поступлений.",
                f"Звезды советуют {sign.name} быть более осмотрительным в тратах.",
                f"Хороший день для финансового планирования и инвестиций.",
                f"Возможно, пришло время пересмотреть свой бюджет.",
                f"Ваша интуиция в финансовых вопросах сегодня особенно остра.",
                f"Не бойтесь рисковать, но помните о разумной осторожности.",
                f"Сегодня благоприятный день для решения старых финансовых проблем."
            ]
            predictions[sign.name]["Личностный рост"] = [
                f"Влияние {sign.ruling_planet}а усилит вашу способность к самопознанию.",
                f"Энергия {sign.element}а поможет вам преодолеть внутренние барьеры.",
                f"Ваше {sign.quality.lower()} качество поможет в достижении личных целей.",
                f"Сегодня {sign.name} может открыть в себе новые таланты и способности.",
                f"Звезды советуют {sign.name} больше времени уделять саморазвитию.",
                f"Хороший день для начала изучения новых навыков или хобби.",
                f"Возможно, пришло время пересмотреть свои жизненные приоритеты.",
                f"Ваша интуиция сегодня может подсказать верное направление развития.",
                f"Не бойтесь выходить из зоны комфорта, это ключ к росту.",
                f"Сегодня благоприятный день для работы над своими слабостями."
            ]
            predictions[sign.name]["Учеба"] = [
                f"Влияние {sign.ruling_planet}а усилит вашу способность к концентрации и запоминанию.",
                f"Энергия {sign.element}а поможет вам легко усваивать новую информацию.",
                f"Ваше {sign.quality.lower()} качество поможет в решении сложных задач.",
                f"Сегодня {sign.name} может сделать важное открытие в процессе обучения.",
                f"Звезды советуют {sign.name} уделить особое внимание самообразованию.",
                f"Хороший день для сдачи экзаменов или прохождения тестов.",
                f"Возможно, стоит пересмотреть свои методы обучения для большей эффективности.",
                f"Ваша любознательность сегодня может привести к неожиданным открытиям.",
                f"Не бойтесь задавать вопросы и искать дополнительную информацию.",
                f"Сегодня благоприятный день для планирования вашего образовательного пути."
            ]
            predictions[sign.name]["Хобби"] = [
                f"Влияние {sign.ruling_planet}а усилит вашу креативность и вдохновение.",
                f"Энергия {sign.element}а поможет вам найти новое увлекательное хобби.",
                f"Ваше {sign.quality.lower()} качество проявится в творческих начинаниях.",
                f"Сегодня {sign.name} может открыть в себе неожиданные таланты.",
                f"Звезды советуют {sign.name} больше времени уделять любимым занятиям.",
                f"Хороший день для экспериментов и пробы чего-то нового.",
                f"Возможно, пришло время вернуться к давно забытому увлечению.",
                f"Ваше хобби сегодня может принести не только удовольствие, но и пользу.",
                f"Не бойтесь делиться своими творческими достижениями с окружающими.",
                f"Сегодня благоприятный день для участия в конкурсах или выставках."
            ]
        return predictions

    def get_zodiac_sign(self, birth_date: datetime.date) -> ZodiacSign:
        for sign in self.zodiac_signs:
            start = datetime.date(birth_date.year, *sign.start_date)
            end = datetime.date(birth_date.year, *sign.end_date)
            if start <= birth_date <= end:
                return sign
        return self.zodiac_signs[-1]

    def generate_astrological_chart(self, birth_date: datetime.date) -> AstrologicalChart:
        zodiac_sign = self.get_zodiac_sign(birth_date)
        ascendant = random.choice(self.zodiac_signs)
        moon_sign = random.choice(self.zodiac_signs)
        return AstrologicalChart(zodiac_sign, ascendant, moon_sign)

    def calculate_compatibility(self, sign1: ZodiacSign, sign2: ZodiacSign) -> float:
        base_compatibility = random.uniform(0.5, 1.0)
        element_bonus = 0.1 if sign1.element == sign2.element else 0
        quality_bonus = 0.1 if sign1.quality == sign2.quality else 0
        return min(base_compatibility + element_bonus + quality_bonus, 1.0)

    def generate_horoscope(self, birth_date: datetime.date, current_date: datetime.date) -> str:
        chart = self.generate_astrological_chart(birth_date)
        zodiac_sign = chart.zodiac_sign
        horoscope = f"Гороскоп для {zodiac_sign.name} {zodiac_sign.symbol} на {current_date.strftime('%d.%m.%Y')}:\n\n"

        for aspect in self.aspects:
            prediction = random.choice(self.predictions[zodiac_sign.name][aspect])
            horoscope += f"{aspect}: {prediction}\n\n"

        lucky_number = random.randint(1, 100)
        lucky_color = self.colors[zodiac_sign.name]

        horoscope += f"Счастливое число: {lucky_number}\n"
        horoscope += f"Счастливый цвет: {lucky_color}\n\n"

        horoscope += f"Астрологическая карта:\n"
        horoscope += f"Солнечный знак: {zodiac_sign.name} {zodiac_sign.symbol}\n"
        horoscope += f"Асцендент: {chart.ascendant.name} {chart.ascendant.symbol}\n"
        horoscope += f"Лунный знак: {chart.moon_sign.name} {chart.moon_sign.symbol}\n\n"

        horoscope += f"Положение планет:\n"
        for planet in chart.planets:
            sign = self.zodiac_signs[math.floor(planet.degrees / 30)]
            horoscope += f"{planet.name} {planet.symbol}: {sign.name} {sign.symbol} ({planet.degrees:.2f}°)\n"

        compatibility = self.calculate_compatibility(zodiac_sign, chart.moon_sign)
        horoscope += f"\nСовместимость с Лунным знаком: {compatibility:.2%}\n"

        horoscope += f"\nСовет дня: {self.get_daily_advice(zodiac_sign)}\n"

        return horoscope

    def get_daily_advice(self, sign: ZodiacSign) -> str:
        advices = [
            f"Сегодня энергия {sign.element}а особенно сильна. Используйте это для достижения своих целей.",
            f"Ваше {sign.quality.lower()} качество поможет вам справиться с неожиданными ситуациями.",
            f"Прислушайтесь к влиянию {sign.ruling_planet}а и доверьтесь своей интуиции.",
            "Сегодня хороший день для медитации и самопознания.",
            "Будьте открыты новым возможностям, они могут прийти с неожиданной стороны.",
            f"Используйте силу {sign.element}а для преодоления препятствий.",
            f"Ваша {sign.quality.lower()} природа сегодня может стать ключом к успеху.",
            f"Обратите внимание на знаки, которые посылает вам {sign.ruling_planet}.",
            "Сегодня благоприятный день для начала новых проектов.",
            "Не бойтесь перемен, они могут открыть перед вами новые горизонты."
        ]
        return random.choice(advices)

class HoroscopeHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.generator = HoroscopeGenerator()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path.startswith("/horoscope"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            query = urlparse(self.path).query
            params = parse_qs(query)
            
            birth_date_str = params.get('birth_date', [''])[0]
            try:
                birth_date = datetime.datetime.strptime(birth_date_str, "%d.%m.%Y").date()
                current_date = datetime.date.today()
                
                horoscope = self.generator.generate_horoscope(birth_date, current_date)
                
                response = json.dumps({"horoscope": horoscope}, ensure_ascii=False)
                self.wfile.write(response.encode('utf-8'))
            except ValueError:
                error_message = json.dumps({"error": "Invalid date format. Please use DD.MM.YYYY"})
                self.wfile.write(error_message.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    server_address = ("192.168.1.4", 8080)
    httpd = HTTPServer(server_address, HoroscopeHandler)
    print("Server running at: http://192.168.1.4:8080")
    httpd.serve_forever()
