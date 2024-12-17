# from PyQt5.QtSql import QSqlQuery

# def execute_query(query: QSqlQuery, query_string: str) -> bool:
#     query.prepare(query_string)
#     if not query.exec_():
#         print(f"Ошибка выполнения запроса: {query_string} - {query.lastError().text()}")
#         return False
#     return True

# def ClassRoomAdd(number: int, name: str) -> int:
#     query = QSqlQuery()
#     insert_query = "INSERT INTO classroom (number, name) VALUES (:number, :name);"
#     query.bindValue(":number", number)
#     query.bindValue(":name", name)

#     if execute_query(query, insert_query):
#         last_id_query = "SELECT LAST_INSERT_ID();"
#         execute_query(query, last_id_query)

#         if query.next():
#             return query.value(0)  
#     return 0  

# def ClassRoomChangeById(id: int, number: int, name: str) -> bool:
#     query = QSqlQuery()
#     update_query = "UPDATE classroom SET number = :number, name = :name WHERE id = :id;"
#     query.bindValue(":number", number)
#     query.bindValue(":name", name)
#     query.bindValue(":id", id)

#     return execute_query(query, update_query) and query.numRowsAffected() > 0 

# def ClassRoomDeleteById(id: int) -> bool:
#     query = QSqlQuery()
#     delete_query = "DELETE FROM classroom WHERE id = :id;"
#     query.bindValue(":id", id)

#     return execute_query(query, delete_query) and query.numRowsAffected() > 0  

import sqlite3

path_to_db = "path_to_your_database.db"  

def execute_query(query_string: str, params: tuple = ()) -> bool:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute(query_string, params)
        connection.commit()
        return True
    except Exception as e:
        print(f"Ошибка выполнения запроса: {query_string} - {e}")
        return False
    finally:
        connection.close()

def ClassRoomAdd(number: int, name: str) -> int:
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO classroom (number, name) VALUES (?, ?)", (number, name))
        connection.commit()
        return cursor.lastrowid  
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return 0
    finally:
        connection.close()

def ClassRoomChangeById(id: int, number: int, name: str) -> bool:
    query_string = "UPDATE classroom SET number = ?, name = ? WHERE id = ?;"
    return execute_query(query_string, (number, name, id))

def ClassRoomDeleteById(id: int) -> bool:
    query_string = "DELETE FROM classroom WHERE id = ?;"
    return execute_query(query_string, (id,))
