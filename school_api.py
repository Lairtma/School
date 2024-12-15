from datetime import datetime, date
import sqlite3

path_to_db = "School.db"

def DefaultScheduleAddLesson(weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int) -> int:
    return 0 # id созданного урока


def DefaultScheduleGetLessonById(id: int) -> list:
    return []

def DefaultScheduleGetLessons() -> list:
    return []

def DefaultScheduleChangeLessonById(id: int, weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int) -> bool:
    return True # удалось поменять или нет

def DefaultScheduleDeleteLessonById(id: int) -> bool:
    return True # удалось удалить или нет

table_name = "teachers"
def TeacherAdd(name: str, surname: str, lastname: str) -> int:
    """Добавление нового учителя"""
    if not name:
        return -1
    if not surname:
        return -1
    if not lastname:
        return -1
    
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(f'INSERT INTO {table_name} (name, surname, lastname)  VALUES (?, ?, ?)', (name, surname, lastname))
        id = cursor.lastrowid
        connection.commit()
        connection.close()
        return id # id добавленного учителя
    except Exception as e:
        print(f"Ошибка: {e}")
        return -1

def TeacherChangeById(id: int, name: str, surname: str, lastname: str) -> bool:
    """Изменение информации об учителе"""
    #UPDATE teachers SET name = ?, surname = ?, lastname = ? WHERE id = ?
    updatefields = {}
    if name:
        updatefields['name'] = name
    if surname:
        updatefields['surname'] = surname
    if lastname:
        updatefields['lastname'] = lastname
    
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        a = ", ".join([f'{field} = ?' for field in updatefields.keys()])
        b = list(updatefields.values())
        b.append(id)
        query = f"UPDATE {table_name} SET {a} WHERE id = ?"
        cursor.execute(query, b)
        connection.commit()
        connection.close()
        return True # удалось поменять или нет
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    


def TeacherDeleteById(id: int) -> bool:
    """Удаление учителя"""
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(f'DELETE FROM {table_name} WHERE id = ?' , id)
        connection.commit()
        connection.close()
        return True # удалось удалить или нет
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def TeacherGetById(id: int) -> list:
    """Получение информации об учителе"""
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
        teacher = cursor.fetchall()
        connection.close()
        return teacher
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def SubjectAdd(name: str) -> int:
    return 0 # id добавленного предмета

def SubjectChangeById(id: int, name: str) -> bool:
    return True # удалось поменять или нет

def SubjectDeleteById(id: int) -> bool:
    return True # удалось удалить или

def ClassRoomAdd(number: int, name: str) -> int:
    return 0 # id добавленного кабинета

def ClassRoomChangeById(id: int, number: int, name: str) -> bool:
    return True # удалось поменять или нет

def ClassRoomDeleteById(id: int) -> bool:
    return True # удалось удалить или нет

def TeacherAndClassRoomAdd(classroom_id: int, teacher_id: int) -> int:
    return 0 # id добавленной связи

def TeacherAndClassRoomChangeById(id: int, classroom_id: int, teacher_id: int) -> bool:
    return True # удалось поменять или нет

def TeacherAndClassRoomDeleteById(id: int) -> bool:
    return True # удалось удалить или нет

def ChangeInScheduleAdd(weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int, lesson_date: date) -> int:
    return 0 # id добавленного изменения

def ChangeInScheduleChangeById(id: int, weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int, lesson_date: date) -> bool:
    return True # удалось поменять или нет

def ChangeInScheduleDeleteById(id: int) -> bool:
    return True # удалось удалить или нет

def ClassRoomGetEmpty(number_of_lesson: int, lesson_date: date) -> list:
    return [] # возвращает список пустых аудиторий в конкретный день и номер урока

def ClassRoomReCalculate(number_of_lesson: int, lesson_date: date) -> bool:
    return True # пересчитывает кабинеты для уроков в определённый урок и день