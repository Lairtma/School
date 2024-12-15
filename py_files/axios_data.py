LESSONS_NUM_TIME = [
            "1\n8:00–8:45", "2\n8:55–9:40", "3\n9:55–10:40",
            "4\n10:55–11:40", "5\n12:00–12:45", "6\n12:55–13:40",
            "7\n13:50–14:35", "8\n14:45–15:30", "9\n15:40–16:25"
        ]

CLASSES_LIST = [
            "1А", "1Б", "1В", "1Г",
            "2А", "2Б", "2В", "2Г",
            "3А", "3Б", "3В", "3Г",
            "4А", "4Б", "4В", "4Г",
            "5А", "5Б", "5В", "5Г",
            "6А", "6Б", "6В", "6Г",
            "7А", "7Б", "7В", "7Г",
            "8А", "8Б", "8В", "8Г",
            "9А", "9Б", "9В", "9Г",
            "10А", "10Б", "10В", "10Г",
            "11А", "11Б", "11В", "11Г"
        ]

WEEK_DAYS = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье"
        ]

SUBJECTS_LIST = [
            "Математика",
            "Русский язык",
            "Литература",
            "История",
            "Физика",
            "Химия",
            "Биология",
            "География",
            "Иностранный язык",
            "Физическая культура"
        ]

TEACHERS = [
    "Иванов А.П.",
    "Смирнова Е.В.",
    "Кузнецов И.М.",
    "Попова Т.С.",
    "Васильев О.Н.",
    "Петрова Л.И.",
    "Соколов Д.А.",
    "Морозова К.П.",
    "Волков С.В.",
    "Фёдорова Н.Ю."
]

PLACES = [ x for x in range (100, 120) ]


LESSONS_TITLE_PLACE_TEACHER_CLASS = {
    WEEK_DAYS[0]: # день недели
    {
        CLASSES_LIST[0]: # класс
        { 
            1: # номер урока
                {
                "group_lesson" : False,
                "title_lesson" : SUBJECTS_LIST[0],
                "teacher" : TEACHERS[0],
                "places" : None
                },
            2: 
                {
                    "group_lesson" : True,
                    "num_subgroups" : 2,
                    "group_1": {
                        "title_lesson" : SUBJECTS_LIST[1],
                        "teacher" : TEACHERS[1],
                        "places" : PLACES[0]
                    },
                    "group_2": {
                        "title_lesson" : SUBJECTS_LIST[2],
                        "teacher" : TEACHERS[2],
                        "places" : PLACES[1]
                    },
                }
        }
    },
}