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