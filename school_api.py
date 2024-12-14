from datetime import datetime, date
import sqlite3

path_to_db = "School.db"

def DefaultScheduleAddLesson(weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int) -> int:
    if not weekday:
        return -1
    if not number_of_lesson:
        return -1
    if not teacher_id:
        return -1
    if not classroom_id:
        return -1
    if not class_id:
        return -1
    if not subject_id:
        return -1
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO default_schedule (weekday, number_of_lesson, teacher_id, room_id, class_id, discipline_id, date_create) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (weekday, number_of_lesson, teacher_id, classroom_id, subject_id, datetime.now()))
    connection.commit()
    connection.close()
    return 0 # id созданного урока


def DefaultScheduleGetLessonById(id: int) -> list:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM default_schedule WHERE id = ?", (id,))
    lessons = cursor.fetchall()
    connection.close()
    return lessons

def DefaultScheduleGetLessons() -> list:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM default_schedule", (id,))
    lessons = cursor.fetchall()
    connection.close()
    return lessons

def DefaultScheduleChangeLessonById(id: int, weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int) -> bool:
    lesson = DefaultScheduleGetLessonById(id)[0]
    if not weekday:
        weekday = lesson[1]
    if not number_of_lesson:
        number_of_lesson = lesson[2]
    if not teacher_id:
        teacher_id = lesson[3]
    if not classroom_id:
        classroom_id = lesson[4]
    if not class_id:
        class_id = lesson[5]
    if not subject_id:
        subject_id = lesson[6]
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("UPDATE default_schedule SET weekday = ?, number_of_lesson = ?, teacher_id = ?, room_id = ?, class_id = ?, discipline_id = ?, date_create = ? WHERE id = ?", (weekday, number_of_lesson, teacher_id, classroom_id, class_id, subject_id, datetime.now(), id))
    connection.commit()
    connection.close()
    return True # удалось поменять или нет

def DefaultScheduleDeleteLessonById(id: int) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM default_schedule WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    return True # удалось удалить или нет

def TeacherAdd(name: str, surname: str, lastname: str) -> int:
    return 0 # id добавленного учителя

def TeacherChangeById(id: int, name: str, surname: str, lastname: str) -> bool:
    return True # удалось поменять или нет

def TeacherDeleteById(id: int) -> bool:
    return True # удалось удалить или нет

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