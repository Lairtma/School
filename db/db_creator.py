from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys
import os

def db_creator():
    # Путь к базе данных
    db_path = "School.db"

    # Удаляем файл базы данных, если он существует (для тестирования)
    if os.path.exists(db_path):
        os.remove(db_path)

    # Создание и настройка базы данных
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)

    if not db.open():
        print("Не удалось открыть базу данных")
        sys.exit(1)
    else:
        print("База данных открыта")

    # Создание таблиц
    query = QSqlQuery()

    create_discipline_table = """
    CREATE TABLE IF NOT EXISTS discipline (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(100)
    );
    """

    create_class_table = """
    CREATE TABLE IF NOT EXISTS class (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(10),
        mini_group VARCHAR(50)
    );
    """

    create_teacher_table = """
    CREATE TABLE IF NOT EXISTS teacher (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        fio VARCHAR(50)
    );
    """

    create_teacher_and_discipline_table = """
    CREATE TABLE IF NOT EXISTS teacher_and_discipline (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        discipline_id INTEGER,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teacher (id),
        FOREIGN KEY (discipline_id) REFERENCES discipline (id)
    );
    """

    create_room_table = """
    CREATE TABLE IF NOT EXISTS room (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        capacity FLOAT,
        name VARCHAR(50)
    );
    """

    create_teacher_and_room_table = """
    CREATE TABLE IF NOT EXISTS teacher_and_room (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        room_id INTEGER,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teacher (id),
        FOREIGN KEY (room_id) REFERENCES room (id)
    );
    """

    create_default_schedule_table = """
    CREATE TABLE IF NOT EXISTS default_schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        weekday INTEGER,
        number_of_lesson INTEGER,
        teacher_id INTEGER,
        room_id INTEGER,
        class_id INTEGER,
        discipline_id INTEGER,
        date_create DATETIME,
        FOREIGN KEY (teacher_id) REFERENCES teacher (id),
        FOREIGN KEY (room_id) REFERENCES room (id),
        FOREIGN KEY (class_id) REFERENCES class (id),
        FOREIGN KEY (discipline_id) REFERENCES discipline (id)
    );
    """

    create_changes_in_schedule_table = """
    CREATE TABLE IF NOT EXISTS changes_in_schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        number_of_lesson INTEGER,
        teacher_id INTEGER,
        room_id INTEGER,
        class_id INTEGER,
        discipline_id INTEGER,
        date_lesson DATE,
        date_change DATETIME,
        is_created_by_user BOOLEAN,
        FOREIGN KEY (teacher_id) REFERENCES teacher (id),
        FOREIGN KEY (room_id) REFERENCES room (id),
        FOREIGN KEY (class_id) REFERENCES class (id),
        FOREIGN KEY (discipline_id) REFERENCES discipline (id)
    );
    """

    # Выполнение запросов для создания таблиц
    if not query.exec_(create_discipline_table):
        print("Ошибка создания таблицы create_discipline_table: ", query.lastError().text())

    if not query.exec_(create_class_table):
        print("Ошибка создания таблицы create_class_table: ", query.lastError().text())

    if not query.exec_(create_teacher_table):
        print("Ошибка создания таблицы create_teacher_table: ", query.lastError().text())

    if not query.exec_(create_teacher_and_discipline_table):
        print("Ошибка создания таблицы create_teacher_and_discipline_table: ", query.lastError().text())

    if not query.exec_(create_room_table):
        print("Ошибка создания таблицы create_room_table: ", query.lastError().text())

    if not query.exec_(create_teacher_and_room_table):
        print("Ошибка создания таблицы create_teacher_and_room_table: ", query.lastError().text())

    if not query.exec_(create_default_schedule_table):
        print("Ошибка создания таблицы create_default_schedule_table: ", query.lastError().text())

    if not query.exec_(create_changes_in_schedule_table):
        print("Ошибка создания таблицы create_changes_in_schedule_table : ", query.lastError().text())

    # Убедитесь, что база данных открыта и создана.

    # Функция для выполнения SQL запросов
    def execute_query(query_string):
        query.prepare(query_string)
        if not query.exec_():
            print(f"Ошибка выполнения запроса: {query_string} - {query.lastError().text()}")

    # Заполнение таблицы predmet
    insert_discipline = """
    INSERT INTO discipline (name) VALUES 
    ('Биология'),
    ('Внеурочная деятельность'),
    ('География'),
    ('ИЗО'),
    ('Иностранный язык'),
    ('Информатика'),
    ('История'),
    ('Литература'),
    ('Литературное чтение'),
    ('Математика'),
    ('Музыка'),
    ('ОБЗР'),
    ('Обществознание'),
    ('ОДНКНР'),
    ('Окружающий мир'),
    ('ОРКСЭ'),
    ('Русский язык'),
    ('Труд'),
    ('Физика'),
    ('Физическая культура'),
    ('Химия'),
    ('Основы предпринимательства'),
    ('РАЗГОВОРЫ О ВАЖНОМ'),
    ('РОССИЯ - МОИ ГОРИЗОНТЫ'),
    ('ФИНАНСОВАЯ ГРАМОТНОСТЬ'),
    ('ПРОГРАММИРОВАНИЕ'),
    ('ПРАКТИКУМ'),
    ('ПЕДАГОГИКА И ПСИХОЛОГИЯ'),
    ('Индивидуальный проект'),
    ('Конструирование'),
    ('ИСТ/РР'),
    ('Исаев'),
    ('Боровик'),
    ('Родословие'),
    ('Спортивные игры'),
    ('Семьеведение'),
    ('Функциональная грамотность'),
    ('Музей и культура'),
    ('Мой родной край'),
    ('Компьютер'),
    ('Технология в современном мире'),
    ('Прикладная информатика'),
    ('Наглядная геометрия'),
    ('Физический практикум'),
    ('Искусство'),
    ('Школа телетворчества'),
    ('Введение в науку'),
    ('ОПК'),
    ('По выбору'),
    ('Решение задач'),
    ('Шахматы'),
    ('РПС'),
    ('Мир движений'),
    ('Азбука здоровья'),
    ('Экскурсионный клуб'),
    ('Практикум по биологии'),
    ('Практикум по русскому языку'),
    ('Практикум по решению задач'),
    ('Scratch-программированеи'),
    ('Программирование Python'),
    ('Коваленко');
    """
    execute_query(insert_discipline)

    # Заполнение таблицы class
    insert_class = """
    INSERT INTO class (name, mini_group) VALUES 
    ('1А', '1 группа'),
    ('1А', '2 группа'),
    ('1А', 'Мальчики'),
    ('1А', 'Девочки'),
    ('1А', 'Весь класс'),
    ('1Б', '1 группа'),
    ('1Б', '2 группа'),
    ('1Б', 'Мальчики'),
    ('1Б', 'Девочки'),
    ('1Б', 'Весь класс'),
    ('1В', '1 группа'),
    ('1В', '2 группа'),
    ('1В', 'Мальчики'),
    ('1В', 'Девочки'),
    ('1В', 'Весь класс'),
    ('1Г', '1 группа'),
    ('1Г', '2 группа'),
    ('1Г', 'Мальчики'),
    ('1Г', 'Девочки'),
    ('1Г', 'Весь класс'),
    ('2А', '1 группа'),
    ('2А', '2 группа'),
    ('2А', 'Мальчики'),
    ('2А', 'Девочки'),
    ('2А', 'Весь класс'),
    ('2Б', '1 группа'),
    ('2Б', '2 группа'),
    ('2Б', 'Мальчики'),
    ('2Б', 'Девочки'),
    ('2Б', 'Весь класс'),
    ('2В', '1 группа'),
    ('2В', '2 группа'),
    ('2В', 'Мальчики'),
    ('2В', 'Девочки'),
    ('2В', 'Весь класс'),
    ('2Г', '1 группа'),
    ('2Г', '2 группа'),
    ('2Г', 'Мальчики'),
    ('2Г', 'Девочки'),
    ('2Г', 'Весь класс'),
    ('3А', '1 группа'),
    ('3А', '2 группа'),
    ('3А', 'Мальчики'),
    ('3А', 'Девочки'),
    ('3А', 'Весь класс'),
    ('3Б', '1 группа'),
    ('3Б', '2 группа'),
    ('3Б', 'Мальчики'),
    ('3Б', 'Девочки'),
    ('3Б', 'Весь класс'),
    ('3В', '1 группа'),
    ('3В', '2 группа'),
    ('3В', 'Мальчики'),
    ('3В', 'Девочки'),
    ('3В', 'Весь класс'),
    ('3Г', '1 группа'),
    ('3Г', '2 группа'),
    ('3Г', 'Мальчики'),
    ('3Г', 'Девочки'),
    ('3Г', 'Весь класс'),
    ('4А', '1 группа'),
    ('4А', '2 группа'),
    ('4А', 'Мальчики'),
    ('4А', 'Девочки'),
    ('4А', 'Весь класс'),
    ('4Б', '1 группа'),
    ('4Б', '2 группа'),
    ('4Б', 'Мальчики'),
    ('4Б', 'Девочки'),
    ('4Б', 'Весь класс'),
    ('4В', '1 группа'),
    ('4В', '2 группа'),
    ('4В', 'Мальчики'),
    ('4В', 'Девочки'),
    ('4В', 'Весь класс'),
    ('4Г', '1 группа'),
    ('4Г', '2 группа'),
    ('4Г', 'Мальчики'),
    ('4Г', 'Девочки'),
    ('4Г', 'Весь класс'),
    ('5А', '1 группа'),
    ('5А', '2 группа'),
    ('5А', 'Мальчики'),
    ('5А', 'Девочки'),
    ('5А', 'Весь класс'),
    ('5Б', '1 группа'),
    ('5Б', '2 группа'),
    ('5Б', 'Мальчики'),
    ('5Б', 'Девочки'),
    ('5Б', 'Весь класс'),
    ('5В', '1 группа'),
    ('5В', '2 группа'),
    ('5В', 'Мальчики'),
    ('5В', 'Девочки'),
    ('5В', 'Весь класс'),
    ('5Л', '1 группа'),
    ('5Л', '2 группа'),
    ('5Л', 'Мальчики'),
    ('5Л', 'Девочки'),
    ('5Л', 'Весь класс'),
    ('6А', '1 группа'),
    ('6А', '2 группа'),
    ('6А', 'Мальчики'),
    ('6А', 'Девочки'),
    ('6А', 'Весь класс'),
    ('6В', '1 группа'),
    ('6В', '2 группа'),
    ('6В', 'Мальчики'),
    ('6В', 'Девочки'),
    ('6В', 'Весь класс'),
    ('6Л', '1 группа'),
    ('6Л', '2 группа'),
    ('6Л', 'Мальчики'),
    ('6Л', 'Девочки'),
    ('6Л', 'Весь класс'),
    ('7А', '1 группа'),
    ('7А', '2 группа'),
    ('7А', 'Мальчики'),
    ('7А', 'Девочки'),
    ('7А', 'Весь класс'),
    ('7Б', '1 группа'),
    ('7Б', '2 группа'),
    ('7Б', 'Мальчики'),
    ('7Б', 'Девочки'),
    ('7Б', 'Весь класс'),
    ('7В', '1 группа'),
    ('7В', '2 группа'),
    ('7В', 'Мальчики'),
    ('7В', 'Девочки'),
    ('7В', 'Весь класс'),
    ('7М', '1 группа'),
    ('7М', '2 группа'),
    ('7М', 'Мальчики'),
    ('7М', 'Девочки'),
    ('7М', 'Весь класс'),
    ('8А', '1 группа'),
    ('8А', '2 группа'),
    ('8А', 'Мальчики'),
    ('8А', 'Девочки'),
    ('8А', 'Весь класс'),
    ('8Б', '1 группа'),
    ('8Б', '2 группа'),
    ('8Б', 'Мальчики'),
    ('8Б', 'Девочки'),
    ('8Б', 'Весь класс'),
    ('8В', '1 группа'),
    ('8В', '2 группа'),
    ('8В', 'Мальчики'),
    ('8В', 'Девочки'),
    ('8В', 'Весь класс'),
    ('8Л', '1 группа'),
    ('8Л', '2 группа'),
    ('8Л', '3 группа'),
    ('8Л', 'Мальчики'),
    ('8Л', 'Девочки'),
    ('8Л', 'Весь класс'),
    ('9А', '1 группа'),
    ('9А', '2 группа'),
    ('9А', 'Мальчики'),
    ('9А', 'Девочки'),
    ('9А', 'Весь класс'),
    ('9Б', '1 группа'),
    ('9Б', '2 группа'),
    ('9Б', 'Мальчики'),
    ('9Б', 'Девочки'),
    ('9Б', 'Весь класс'),
    ('9В', '1 группа'),
    ('9В', '2 группа'),
    ('9В', 'Мальчики'),
    ('9В', 'Девочки'),
    ('9В', 'Весь класс'),
    ('9Л', '1 группа'),
    ('9Л', '2 группа'),
    ('9Л', 'Мальчики'),
    ('9Л', 'Девочки'),
    ('9Л', 'Весь класс'),
    ('10А', 'ИТ'),
    ('10А', 'СЭ'),
    ('10А', 'Мальчики'),
    ('10А', 'Девочки'),
    ('10А', 'Весь класс'),
    ('11А', '1 группа'),
    ('11А', '2 группа'),
    ('11А', 'СЭ'),
    ('11А', 'ИНЖ'),
    ('11А', 'ИТ'),
    ('11А', 'Мальчики'),
    ('11А', 'Девочки'),
    ('11А', 'Весь класс'),
    ('11Б', 'ОБ'),
    ('11Б', 'ОЛ'),
    ('11Б', 'Мальчики'),
    ('11Б', 'Девочки'),
    ('11Б', 'Весь класс'),
    ('Исаев', '1 группа'),
    ('Исаев', '2 группа'),
    ('Исаев', 'Мальчики'),
    ('Исаев', 'Девочки'),
    ('Исаев', 'Весь класс'),
    ('Боровик', '1 группа'),
    ('Боровик', '2 группа'),
    ('Боровик', 'Мальчики'),
    ('Боровик', 'Девочки'),
    ('Боровик', 'Весь класс'),
    ('Коваленко', '1 группа'),
    ('Коваленко', '2 группа'),
    ('Коваленко', 'Мальчики'),
    ('Коваленко', 'Девочки'),
    ('Коваленко', 'Весь класс');
    """
    execute_query(insert_class)

    # Заполнение таблицы prepod
    insert_teacher = """
    INSERT INTO teacher (fio) VALUES 
    ('Алимова И.Ш'),
    ('Анопочкина А.М'),
    ('Бевз Е.С'),
    ('Боярова М.С'),
    ('Бушина М.С'),
    ('Георгиевская Н.М'),
    ('Голуб Ю.Н'),
    ('Дюмина И.А'),
    ('Егорова О.М'),
    ('Емельянцева М.С'),
    ('Емец О.Г'),
    ('Ермакова Я.В'),
    ('Ершова А.Д'),
    ('Клементьева Е.Д'),
    ('Клочкова Т.В'),
    ('Кобякова В.А'),
    ('Козлов С.Л'),
    ('Константинова Е.В'),
    ('Котелова М.Н'),
    ('Кретова В.Д'),
    ('Крымов Ф.С'),
    ('Курцева Д.Ю'),
    ('Латышев В.Н'),
    ('Лебедева В.А'),
    ('Максимова М.В'),
    ('Маслеников К.Ю'),
    ('Мурашкина Т.Р'),
    ('Монастырук Л.И'),
    ('Морозова Л.Г'),
    ('Морозова Т.В'),
    ('Нечаева В.А'),
    ('Никишкина Е.А'),
    ('Оканева О.Е'),
    ('Орлова Е.В'),
    ('Оспинникова С.М'),
    ('Пантелеенко Ю.Р'),
    ('Парамонова Т.Л'),
    ('Половинщиков А.В'),
    ('Пчелова Н.А'),
    ('Ракчеева И.Н'),
    ('Рогачева Ю.А'),
    ('Рощина И.А'),
    ('Сахневич Н.Н'),
    ('Сидорина В.Е'),
    ('Сергеева Н.А'),
    ('Скрипцова А.А'),
    ('Соколова Е.А'),
    ('Соколова Е.В'),
    ('Стецюк Т.В'),
    ('Темкина Е.И'),
    ('Тимохович Е.В'),
    ('Тишина Г.К'),
    ('Толкушкина А.И'),
    ('Торба И.А');
    """
    execute_query(insert_teacher)

    # Заполнение таблицы prepod_and_predmet
    insert_teacher_and_discipline = """
    INSERT INTO teacher_and_discipline (discipline_id, teacher_id) VALUES 
    (5, 1),
    (9, 2),
    (10, 2),
    (15, 2),
    (17, 2),
    (18, 2),
    (23, 2),
    (37, 2),
    (49, 2),
    (53, 2),
    (55, 2),
    (54, 2),
    (52, 2),
    (23, 3),
    (5, 3),
    (24, 3),
    (20, 4),
    (35, 4),
    (23, 5),
    (5, 5),
    (17, 5),
    (8, 5),
    (36, 5),
    (37, 5),
    (17, 6),
    (8, 6),
    (31, 6),
    (30, 7),
    (17, 7),
    (18, 7),
    (9, 7),
    (15, 7),
    (10, 7),
    (23, 7),
    (49, 7),
    (37, 7),
    (52, 7),
    (54, 7),
    (55, 7),
    (53, 7),
    (23, 8),
    (24, 8),
    (7, 8),
    (25, 8),
    (13, 8),
    (33, 8),
    (34, 8),
    (38, 8),
    (10, 9),
    (12, 9),
    (61, 9),
    (30, 10),
    (15, 10),
    (17, 10),
    (18, 10),
    (10, 10),
    (9, 10),
    (23, 10),
    (37, 10),
    (55, 10),
    (54, 10),
    (53, 10),
    (52, 10),
    (23, 11),
    (5, 11),
    (24, 11),
    (23, 12),
    (24, 12),
    (7, 12),
    (13, 12),
    (25, 12),
    (31, 12),
    (22, 12),
    (30, 13),
    (9, 13),
    (15, 13),
    (17, 13),
    (18, 13),
    (10, 13),
    (23, 13),
    (37, 13),
    (51, 13),
    (52, 13),
    (54, 13),
    (53, 13),
    (23, 14),
    (24, 14),
    (7, 14),
    (13, 14),
    (25, 14),
    (22, 14),
    (39, 14),
    (9, 15),
    (10, 15),
    (15, 15),
    (17, 15),
    (18, 15),
    (23, 15),
    (37, 15),
    (49, 15),
    (53, 15),
    (55, 15),
    (54, 15),
    (52, 15),
    (30, 16),
    (15, 16),
    (9, 16),
    (17, 16),
    (18, 16),
    (10, 16),
    (23, 16),
    (37, 16),
    (54, 16),
    (53, 16),
    (40, 16),
    (52, 16),
    (12, 17),
    (18, 17),
    (30, 18),
    (15, 18),
    (9, 18),
    (18, 18),
    (17, 18),
    (10, 18),
    (23, 18),
    (37, 18),
    (55, 18),
    (54, 18),
    (53, 18),
    (52, 18),
    (30, 19),
    (18, 19),
    (17, 19),
    (15, 19),
    (10, 19),
    (9, 19),
    (23, 19),
    (37, 19),
    (55, 19),
    (54, 19),
    (53, 19),
    (52, 19),
    (5, 20),
    (18, 21),
    (23, 22),
    (5, 22),
    (12, 22),
    (24, 22),
    (37, 22),
    (36, 22),
    (26, 23),
    (6, 23),
    (40, 23),
    (42, 23),
    (59, 23),
    (60, 23),
    (24, 23),
    (23, 23),
    (41, 23),
    (5, 24),
    (23, 24),
    (33, 24),
    (36, 24),
    (5, 25),
    (16, 25),
    (14, 25),
    (48, 25),
    (49, 25),
    (10, 26),
    (23, 27),
    (24, 27),
    (4, 27),
    (45, 27),
    (10, 28),
    (15, 28),
    (17, 28),
    (18, 28),
    (9, 28),
    (23, 28),
    (49, 28),
    (37, 28),
    (53, 28),
    (55, 28),
    (54, 28),
    (52, 28),
    (23, 29),
    (24, 29),
    (10, 29),
    (43, 29),
    (8, 30),
    (17, 30),
    (27, 30),
    (31, 30),
    (57, 30),
    (23, 31),
    (24, 31),
    (10, 31),
    (50, 31),
    (37, 31),
    (30, 32),
    (17, 32),
    (15, 32),
    (10, 32),
    (9, 32),
    (18, 32),
    (23, 32),
    (37, 32),
    (51, 32),
    (52, 32),
    (53, 32),
    (54, 32),
    (19, 33),
    (27, 33),
    (44, 33),
    (61, 33),
    (23, 34),
    (24, 34),
    (6, 34),
    (26, 34),
    (33, 34),
    (1, 35),
    (37, 35),
    (47, 35),
    (56, 35),
    (30, 36),
    (15, 36),
    (17, 36),
    (10, 36),
    (9, 36),
    (18, 36),
    (23, 36),
    (37, 36),
    (52, 36),
    (53, 36),
    (54, 36),
    (30, 37),
    (9, 37),
    (17, 37),
    (18, 37),
    (10, 37),
    (15, 37),
    (23, 37),
    (37, 37),
    (38, 37),
    (52, 37),
    (54, 37),
    (53, 37),
    (23, 38),
    (24, 38),
    (20, 38),
    (35, 38),
    (23, 39),
    (24, 39),
    (10, 39),
    (36, 39),
    (23, 40),
    (11, 40),
    (45, 40),
    (36, 40),
    (17, 41),
    (27, 41),
    (8, 41),
    (57, 41),
    (61, 41),
    (23, 42),
    (17, 42),
    (8, 42),
    (33, 42),
    (36, 42),
    (23, 43),
    (24, 43),
    (19, 43),
    (27, 43),
    (18, 43),
    (20, 44),
    (35, 44),
    (21, 45),
    (36, 45),
    (27, 45),
    (30, 46),
    (18, 46),
    (17, 46),
    (15, 46),
    (10, 46),
    (9, 46),
    (23, 46),
    (37, 46),
    (52, 46),
    (53, 46),
    (54, 46),
    (23, 47),
    (24, 47),
    (3, 47),
    (33, 47),
    (40, 47),
    (36, 47),
    (23, 48),
    (24, 48),
    (3, 48),
    (37, 48),
    (18, 49),
    (23, 49),
    (37, 49),
    (53, 49),
    (55, 49),
    (54, 49),
    (52, 49),
    (23, 50),
    (5, 50),
    (24, 50),
    (61, 50),
    (8, 51),
    (30, 52),
    (15, 52),
    (10, 52),
    (9, 52),
    (17, 52),
    (18, 52),
    (23, 52),
    (49, 52),
    (37, 52),
    (52, 52),
    (53, 52),
    (54, 52),
    (17, 53),
    (9, 53),
    (10, 53),
    (15, 53),
    (18, 53),
    (30, 53),
    (23, 53),
    (37, 53),
    (52, 53),
    (53, 53),
    (54, 53),
    (23, 54),
    (24, 54),
    (17, 54),
    (8, 54),
    (31, 54),
    (57, 54);
    """
    execute_query(insert_teacher_and_discipline)

    # Заполнение таблицы kabinet
    insert_room = """
    INSERT INTO room (capacity, name) VALUES 
    (0.5, '320а'),
    (1, '320'),
    (1, '319'),
    (1, '318'),
    (0.5, '316'),
    (1, '314'),
    (1, '312'),
    (1, '311'),
    (0.5, '310'),
    (0.5, '309'),
    (1, '308'),
    (1, '307'),
    (1, '306'),
    (1, '305'),
    (1, '304'),
    (1, '303'),
    (1, '302'),
    (0.5, '301'),
    (1, '219'),
    (1, '218'),
    (1, '217'),
    (1, '215'),
    (1, '214'),
    (1, '213'),
    (1, '212'),
    (1, '211'),
    (1, '210'),
    (1, '209'),
    (1, '208'),
    (1, '207'),
    (1, '206'),
    (1, '205'),
    (1, '116'),
    (1, '112'),
    (1, '113'),
    (1, '108'),
    (1, '109'),
    (1, '110'),
    (1, 'МСЗ'),
    (1, 'БСЗ1'),
    (1, 'БСЗ2'),
    (1, 'Акт зал');
    """
    execute_query(insert_room)

    # Заполнение таблицы prepod_and_kabinet
    insert_teacher_and_room = """
    INSERT INTO teacher_and_room (room_id, teacher_id) VALUES 
    (5, 1),
    (32, 2),
    (37, 2),
    (39, 4),
    (40, 4),
    (41, 4),
    (19, 6),
    (8, 6),
    (16, 7),
    (32, 7),
    (20, 8),
    (25, 9),
    (5, 9),
    (4, 9),
    (5, 11),
    (10, 11),
    (12, 11),
    (19, 12),
    (15, 13),
    (26, 14),
    (14, 15),
    (37, 15),
    (17, 18),
    (36, 19),
    (5, 20),
    (5, 22),
    (12, 22),
    (2, 23),
    (10, 24),
    (12, 25),
    (25, 26),
    (11, 27),
    (14, 28),
    (28, 28),
    (19, 30),
    (21, 30),
    (25, 31),
    (38, 32),
    (22, 33),
    (2, 34),
    (33, 35),
    (31, 37),
    (39, 38),
    (40, 38),
    (41, 38),
    (25, 39),
    (27, 39),
    (42, 40),
    (22, 43),
    (39, 44),
    (40, 44),
    (41, 44),
    (6, 45),
    (23, 48),
    (5, 50),
    (12, 50),
    (37, 52),
    (30, 53),
    (19, 54),
    (7, 54);
    """
    execute_query(insert_teacher_and_room)

    # Заполнение таблицы default_schedule
    insert_default_schedule = """
    INSERT INTO default_schedule (weekday, number_of_lesson, teacher_id, room_id, class_id, discipline_id, date_create) VALUES 
    (1, 1, 1, 1, 1, 1, '2023-10-03 08:00:00'), 
    (1, 2, 2, 2, 1, 2, '2023-10-03 09:00:00'), 
    (2, 1, 1, 1, 2, 3, '2023-10-04 08:00:00'), 
    (2, 2, 2, 2, 2, 4, '2023-10-04 09:00:00');
    """
    execute_query(insert_default_schedule)

    # Заполнение таблицы changes_in_schedule
    insert_changes_in_schedule = """
    INSERT INTO changes_in_schedule (number_of_lesson, teacher_id, room_id, class_id, discipline_id, date_lesson, date_change, is_created_by_user) VALUES 
    (1, 1, 1, 1, 1, '2023-10-03', '2023-10-02 15:00:00', true), 
    (2, 2, 2, 2, 2, '2023-10-04', '2023-10-03 15:00:00', false);
    """
    execute_query(insert_changes_in_schedule)

    print("База данных успешно заполнена")

    execute_query("SELECT * FROM class")
    execute_query("SELECT * FROM discipline")
    execute_query("SELECT * FROM teacher")
    # Закрываем базу данных
    db.close()

    print("База данных и таблицы успешно созданы!")





