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
    last_inserted_id = cursor.lastrowid
    connection.close()
    return last_inserted_id # id созданного урока


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

def ChangesInScheduleGetLessonById(id: int) -> list:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM changes_in_schedule WHERE id = ?", (id,))
        lessons = cursor.fetchall()
        return lessons
    except Exception as e:
        print(f"Ошибка: {e}")
        return []
    finally:
        connection.close()

def ChangeInScheduleAdd(number_of_lesson: int, teacher_id: int, classroom_id: int, class_id:int, subject_id:int, lesson_date: date) -> int:
    if (not number_of_lesson or not teacher_id or not classroom_id or not class_id or not subject_id or not lesson_date):
        return -1
    else:
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO changes_in_schedule ("
                           "number_of_lesson, "
                           "teacher_id, "
                           "room_id, "
                           "class_id, "
                           "discipline_id, "
                           "date_lesson, "
                           "date_change, "
                           "is_created_by_user)"
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (
                            number_of_lesson,
                            teacher_id,
                            classroom_id,
                            class_id,
                            subject_id,
                            lesson_date,
                            datetime.now(),
                            1))
            connection.commit()
            last_inserted_id = cursor.lastrowid
            return last_inserted_id
        except Exception as e:
            print(f"Ошибка: {e}")
            return -1
        finally:
            connection.close()


def ChangeInScheduleChangeById(id: int,
                               number_of_lesson: int = None,
                               teacher_id: int = None,
                               classroom_id: int = None,
                               class_id: int = None,
                               subject_id: int = None,
                               lesson_date: date = None) -> bool:
    lesson = ChangesInScheduleGetLessonById(id)[0]
    if number_of_lesson is None:
        number_of_lesson = lesson[1]
    if teacher_id is None:
        teacher_id = lesson[2]
    if classroom_id is None:
        classroom_id = lesson[3]
    if class_id is None:
        class_id = lesson[4]
    if subject_id is None:
        subject_id = lesson[5]
    if lesson_date is None:
        lesson_date = lesson[6]

    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE changes_in_schedule "
                       "SET number_of_lesson = ?, "
                       "teacher_id = ?, "
                       "room_id = ?, "
                       "class_id = ?, "
                       "discipline_id = ?, "
                       "date_lesson = ?, "
                       "date_change = ?, "
                       "is_created_by_user = ? WHERE id = ?",
                       (
                           number_of_lesson,
                           teacher_id,
                           classroom_id,
                           class_id,
                           subject_id,
                           lesson_date,
                           datetime.now(),
                           1,
                           id
                       ))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        connection.close()


def ChangeInScheduleDeleteById(id: int) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM changes_in_schedule WHERE id = ?", (id,))
        if cursor.rowcount > 0:
            connection.commit()
            return True
        else:
            return False
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        connection.close()

def ClassRoomGetEmpty(number_of_lesson: int, lesson_date: date) -> list:
    return [] # возвращает список пустых аудиторий в конкретный день и номер урока

def ClassRoomReCalculate(number_of_lesson: int, lesson_date: date) -> bool:
    return True # пересчитывает кабинеты для уроков в определённый урок и день