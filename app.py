from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    sections = [
        {
            'id': 1,
            'title': 'История термина «Холодная война»',
            'subtitle': '1947',
            'description': 'Термин «холодная война» впервые использовал Бернард Барух, советник президента США. Это геополитическое, военное и экономическое противостояние между СССР и США, которое длилось с 1946 по 1991 год.',
            'image': 'static/images/1.png'
        },
        {
            'id': 2,
            'title': 'История и начало холодной войны',
            'subtitle': '1946-1953',
            'description': 'Период активного противостояния. «Длинная телеграмма» Кеннана и речи Черчилля в Фултоне. Доктрина Трумэна, план Маршалла и создание НАТО.\n'
            'с одной стороны, и формирование социалистического лагеря с другой, окончательно разделили мир на два противоборствующих блока.',
            'image': 'static/images/2.png'
        },
        {
            'id': 3,
            'title': 'Оттепель и кризисы',
            'subtitle': '1953-1962',
            'description': 'Период характеризовался серией международных кризисов: Берлинский кризис, восстание в Венгрии, строительство Берлинской стены и кульминация\n'
            '- Карибский кризис 1962 года. После смерти Сталина началаь "оттепель" в международных отношениях, но гонка вооружений продолжалась.',
            'image': 'static/images/3.png'
        },
        {
            'id': 4,
            'title': 'Разрядка международной напряженности',
            'subtitle': '1962-1979',
            'description': 'Этап относительной стабилизации отношений между СССР и США. Подписание договоров об ограничении стратегических вооружений (ОСВ-1б ОСВ-2), установление прямой связи между Москвой и Вашингтоном\n'
            ', Хельсикские соглашения 1975 года. Однако ввод советских войск в Афганистан в 1979 году привел к новому витку напряжённости.',
            'image': 'static/images/4.png'
        },
        {
            'id': 5,
            'title': 'Завершение холодной войны',
            'subtitle': '1987-1991',
            'description': '«Новое мышление» Горбачёва, вывод советских войск из Афганистана, падение Берлинской стены и революции в странах Восточной Европы. Распад СССР в 1991 году ознаменовал\n'
            'конец холодной войны и биполярной системы международных отношений. Завершение самого длительного геополитического противостояния XX века.',
            'image': 'static/images/5.png'
        }
    ]
    return render_template('index.html', sections=sections)


questions = [
    {
        "id": 1,
        "question": "Когда началась Холодная война?",
        "options": ["1945", "1946", "1947", "1948"],
        "correct": "1946"
    },
    {
        "id": 2,
        "question": "Кто был лидером СССР во время Холодной войны?",
        "options": ["Иосиф Сталин", "Никита Хрущев", "Леонид Брежнев", "Михаил Горбачев"],
        "correct": "Иосиф Сталин"
    },
    {
        "id": 3,
        "question": "Как называлась политика США по отношению к СССР во время Холодной войны?",
        "options": ["Политика сдерживания", "Политика контеймента", "Политика детанта", "Политика изоляционизма"],
        "correct": "Политика сдерживания"
    },
    {
        "id": 4,
        "question": "Какой был основной фактор Холодной войны?",
        "options": ["Идеологические разногласия", "Экономические интересы", "Политические разногласия", "Военные конфликты"],
        "correct": "Идеологические разногласия"
    },
    {
        "id": 5,
        "question": "Как называлась организация, созданная для противостояния СССР во время Холодной войны?",
        "options": ["НАТО", "ООН", "ЕС", "Совет Безопасности"],
        "correct": "НАТО"
    },
    {
        "id": 6,
        "question": "Какой был результат Берлинского кризиса 1961 года?",
        "options": ["Построение Берлинской стены", "Ввод советских войск в Берлин", "Эвакуация советских войск из Берлина", "Подписание мирного договора"],
        "correct": "Построение Берлинской стены"
    },
    {
        "id": 7,
        "question": "Как называлась политика США по отношению к СССР во время правления президента Рейгана?",
        "options": ["Политика сдерживания", "Политика контеймента", "Политика детанта", "Политика изоляционизма"],
        "correct": "Политика контеймента"
    },
    {
        "id": 8,
        "question": "Какой был результат Карибского кризиса 1962 года?",
        "options": ["Нападение США на Кубу", "Ввод советских войск на Кубу", "Подписание мирного договора", "Обмен пленными"],
        "correct": "Подписание мирного договора"
    },
    {
        "id": 9,
        "question": "Как называлась организация, созданная для экономического сотрудничества между СССР и другими социалистическими странами?",
        "options": ["СЭВ", "ООН", "ЕС", "Совет Безопасности"],
        "correct": "СЭВ"
    },
    {
        "id": 10,
        "question": "Какой был результат Венгерского восстания 1956 года?",
        "options": ["Победа восставших", "Поражение восставших", "Ввод советских войск в Венгрию", "Объявление независимости"],
        "correct": "Поражение восставших"
    },
    {
        "id": 11,
        "question": "Как называлась политика СССР по отношению к США во время Холодной войны?",
        "options": ["Политика сдерживания", "Политика контеймента", "Политика детанта", "Политика изоляционизма"],
        "correct": "Политика сдерживания"
    },
    {
        "id": 12,
        "question": "Какой был результат Афганской войны 1979-1989 годов?",
        "options": ["Победа СССР", "Поражение СССР", "Вывод советских войск из Афганистана", "Объявление независимости"],
        "correct": "Поражение СССР"
    },
    {
        "id": 13,
        "question": "Как называлась организация, созданная для военного сотрудничества между СССР и другими социалистическими странами?",
        "options": ["ОВД", "ООН", "ЕС", "Совет Безопасности"],
        "correct": "ОВД"
    },
    {
        "id": 14,
        "question": "Какой был результат Чехословацкого кризиса 1968 года?",
        "options": ["Победа восставших", "Поражение восставших", "Ввод советских войск в Чехословакию", "Объявление независимости"],
        "correct": "Поражение восставших"
    },
    {
        "id": 15,
        "question": "Как называлась политика США по отношению к СССР во время правления президента Кеннеди?",
        "options": ["Политика сдерживания", "Политика контеймента", "Политика детанта", "Политика изоляционизма"],
        "correct": "Политика сдерживания"
    },
    {
        "id": 16,
        "question": "Какой был результат Кубинской революции 1959 года?",
        "options": ["Победа революционеров", "Поражение революционеров", "Ввод советских войск на Кубу", "Объявление независимости"],
        "correct": "Победа революционеров"
    },
    {
        "id": 17,
        "question": "Как называлась организация, созданная для экономического сотрудничества между США и другими западными странами?",
        "options": ["ОЭСР", "ООН", "ЕС", "Совет Безопасности"],
        "correct": "ОЭСР"
    },
    {
        "id": 18,
        "question": "Какой был результат Вьетнамской войны 1959-1975 годов?",
        "options": ["Победа США", "Поражение США", "Вывод американских войск из Вьетнама", "Объявление независимости"],
        "correct": "Поражение США"
    },
    {
        "id": 19,
        "question": "Как называлась политика СССР по отношению к США во время правления президента Горбачева?",
        "options": ["Политика сдерживания", "Политика контеймента", "Политика детанта", "Политика изоляционизма"],
        "correct": "Политика детанта"
    },
    {
        "id": 20,
        "question": "Какой был результат распада СССР в 1991 году?",
        "options": ["Победа коммунизма", "Поражение коммунизма", "Объявление независимости", "Восстановление монархии"],
        "correct": "Поражение коммунизма"
    }
]


@app.route('/test')
def test():
    return render_template('test.html', questions=questions)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
    