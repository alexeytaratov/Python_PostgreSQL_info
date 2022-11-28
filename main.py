import psycopg2
from config import host, user, password, db_name, port, cursor, connection

try:
    connection = psycopg2.connect( # Функция, которая находится внутри модуля psycopg2.
                                   # Она нужна для подключения базы данных в проект.
                                   # Далее, все эти переменные будут сохранены в переменной.
        host=host,
        dbname=db_name,
        user=user,
        password=password,
        port=port
    )

    cursor = connection.cursor() # Открываем "курсор"

    cursor.execute('DROP TABLE IF EXISTS nice_cars') # Если таблица создана, то удаляем её,
                                                     # так как дальше всё равно создаём.

    create_script = '''CREATE TABLE IF NOT EXISTS nice_cars ( 
        id int PRIMARY KEY,
        name varchar(40) NOT NULL,
        price int NOT NULL)'''
    # Выше создал скрипт, который будет создавать новую таблицу в базу данных.
    # 1 строчка - СОЗДАТЬ ТАБЛИЦУ, ЕСЛИ ТАКАЯ ТАБЛИЦА ЕЩЁ НЕ СОЗДАНА, найс_карс;
    # 2-4 строчки - создаём столбцы этой таблицы

    cursor.execute(create_script) # Теперь, чтобы выполнить скрипт, который хранится в переменной,
                                  # вызываем этот метод и в него передаём имя переменной.

    insert_script = 'INSERT INTO nice_cars (id, name, price) VALUES (%s, %s, %s)' # в этой строке будем добавлять всякую всячину в нашу таблицу
    insert_value = (1, 'Lada', 1200000) # эти значения будут вставляться вместо процентов
    cursor.execute(insert_script, insert_value) # Теперь, чтобы выполнить скрипт, который хранится в переменной,
                                                # вызываем этот метод и в него передаём имя переменной.
    # !!! ВАЖНО !!!
    # Добавлять можно только не повторяющиеся строки. То есть после того, как скрипт отработал, можно его закомментить.
    # А можно удалять и создавать новую таблицу каждый раз, перед тем, как её заполнить.

    # Также, если бы нам надо было передать сказу несколько строк в таблицу, то:
    # for i in insert_value: (при этом внутри этой переменной список из строк: [(1, 'Lada', 1200000), (2, 'Mers', 3000345)], например)
        # cursor.execute(insert_script, i)

    cursor.execute('SELECT * FROM nice_cars') # выполняет запрос на получение всех данных из таблицы в БД
    for i in cursor.fetchall(): # Метод для того, чтобы просмотреть все записи, которые были в курсор записаны
        print(i) # Построчно выводим данные из курсора

    update_script = 'UPDATE nice_cars SET price = price + (price + 50000)' # тут изменяем один из столбцов
    cursor.execute(update_script)

    delete_script = 'DELETE FROM nice_cars WHERE name = %s' # тут удаляем строки по условию WHERE
    delete_record = ('Lada',) # Тут написано, кого удаляем. Запятая обязательна.
    cursor.execute(delete_script, delete_record) # сюда два аргумента


    connection.commit() # Этот метод сохраняет любые изменения, которые мы делаем в базе данных.
                        # Его обязательно нужно вызывать.

except Exception as error: # Если в коде ТРАЙ ошибка, то выводим это.
    print(error)

finally: # Этот блок кода выполняется в любом случае
    if cursor is not None: # Если переменная "курсор" была изменена, то закрыть
        cursor.close()  # Закрываем "курсор"
    if connection is not None:  # Если переменная "коннекшен" была изменена, то закрыть
        connection.close()  # После того, как подключили базы данных, их надо отключить.
