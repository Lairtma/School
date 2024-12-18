from datetime import datetime, date
import sqlite3

path_to_db = "School.db"



def DefaultScheduleAddLesson(weekday: int, number_of_lesson: int, teacher_id: int, classroom_id: int, class_id: int,
                             subject_id: int) -> int:
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
    cursor.execute(
        "INSERT INTO default_schedule (weekday, number_of_lesson, teacher_id, room_id, class_id, discipline_id, date_create) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (weekday, number_of_lesson, teacher_id, classroom_id, class_id, subject_id, datetime.now()))
    connection.commit()
    last_inserted_id = cursor.lastrowid
    connection.close()
    return last_inserted_id  # id созданного урока


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
    cursor.execute("SELECT * FROM default_schedule")
    lessons = cursor.fetchall()
    connection.close()
    return lessons


def DefaultScheduleChangeLessonById(id: int, weekday: int = None, number_of_lesson: int = None, teacher_id: int = None,
                                    classroom_id: int = None, class_id: int = None, subject_id: int = None) -> bool:
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
    cursor.execute(
        "UPDATE default_schedule SET weekday = ?, number_of_lesson = ?, teacher_id = ?, room_id = ?, class_id = ?, discipline_id = ?, date_create = ? WHERE id = ?",
        (weekday, number_of_lesson, teacher_id, classroom_id, class_id, subject_id, datetime.now(), id))
    connection.commit()
    connection.close()
    return True  # удалось поменять или нет


def DefaultScheduleDeleteLessonById(id: int) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM default_schedule WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    return True  # удалось удалить или нет


def TeacherAdd(fio: str) -> int:
    """Добавление нового учителя"""
    if not fio:
        return -1
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO teacher (fio)  VALUES (?)",(fio,))
        id = cursor.lastrowid
        connection.commit()
        connection.close()
        return id  # id добавленного учителя
    except Exception as e:
        print(f"Ошибка: {e}")
        return -1

def TeacherGetById(id: int) -> int:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM teacher WHERE id = ?", (id,))
        teachers = cursor.fetchall()
        return teachers
    except Exception as e:
        print(f"Ошибка: {e}")
        return []
    finally:
        connection.close()


def TeacherChangeById(id: int, fio: str) -> bool:
    """Изменение информации об учителе"""
    table_name = "teacher"
    try:
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        query = f"UPDATE {table_name} SET fio = ? WHERE id = ?"
        cursor.execute(query, (fio, id))
        connection.commit()
        connection.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Ошибка обновления предмета: {e}")
        return False


def TeacherDeleteById(id: int) -> bool:
    """Удаление учителя"""
    table_name = "teacher"
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', (id,))
        connection.commit()
        connection.close()
        return True # удалось удалить или нет
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def SubjectAdd(name: str) -> int:
    table_name = "discipline"
    """Добавление нового предмета в таблицу."""
    if not name:
        return -1  # Возвращаем -1, если имя не указано
    try:
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {table_name} (name) VALUES (?)", (name,))
        id = cursor.lastrowid  # Получаем ID добавленной строки
        connection.commit()
        connection.close()
        return id
    except Exception as e:
        print(f"Ошибка добавления предмета: {e}")
        return -1

def SubjectChangeById(id: int, name: str) -> bool:
    table_name = "discipline"
    """Обновление названия предмета по ID."""
    if not id or not name:
        return False
    try:
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        query = f"UPDATE {table_name} SET name = ? WHERE id = ?"
        cursor.execute(query, (name, id))
        connection.commit()
        connection.close()
        return cursor.rowcount > 0  # Возвращаем True, если строки были обновлены
    except Exception as e:
        print(f"Ошибка обновления предмета: {e}")
        return False


def SubjectDeleteById(id: int) -> bool:
    """Удаление предмета по ID."""
    table_name = "discipline"
    if not id:
        return False
    try:
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        query = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(query, (id,))
        connection.commit()
        connection.close()
        return cursor.rowcount > 0  # Возвращаем True, если строки были удалены
    except Exception as e:
        print(f"Ошибка удаления предмета: {e}")
        return False


def ClassRoomAdd(name: str, capacity: float=None) -> int:
    if not capacity:
        capacity = 1
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO room (name, capacity) VALUES (?, ?)", (name, capacity))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return -1
    finally:
        connection.close()


def ClassRoomChangeById(id: int, name: str, capacity: float) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE room SET name = ?, capacity = ? WHERE id = ?", (name, capacity, id))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return False
    finally:
        connection.close()


def ClassRoomDeleteById(id: int) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM room WHERE id = ?", (id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return False
    finally:
        connection.close()


def TeacherAndClassRoomAdd(classroom_id: int, teacher_id: int) -> int:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO teacher_and_room (room_id, teacher_id) VALUES (?, ?)", (classroom_id, teacher_id))
        teacher_and_room_add = cursor.fetchall()
        last_inserted_id = cursor.lastrowid
        return last_inserted_id
    except Exception as e:
        print(f"Ошибка: {e}")
        return -1
    finally:
        connection.close()


import sqlite3

def TeacherAndClassRoomChangeById(id: int, classroom_id: int, teacher_id: int) -> bool:
    try:
        with sqlite3.connect(path_to_db) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE teacher_and_room SET room_id = ?, teacher_id = ? WHERE id = ?",
                (classroom_id, teacher_id, id),
            )
            connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        connection.close()


def TeacherAndClassRoomDeleteById(id: int) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM teacher_and_room WHERE id = ?", (id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        connection.close()


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


def ChangeInScheduleAdd(number_of_lesson: int, teacher_id: int, classroom_id: int, class_id: int, subject_id: int,
                        lesson_date: date) -> int:
    if (
            not number_of_lesson or not teacher_id or not classroom_id or not class_id or not subject_id or not lesson_date):
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
    return []  # возвращает список пустых аудиторий в конкретный день и номер урока


def ClassRoomReCalculate(number_of_lesson: int, lesson_date: date) -> bool:
    return True  # пересчитывает кабинеты для уроков в определённый урок и день