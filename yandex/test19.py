import sqlite3 as sl
import sys

def add_table(con):
    # открываем базу
    with con:
        # получаем количество таблиц с нужным нам именем
        data = con.execute("select count(*) from sqlite_master where type='table' and name='meetings'")
        for row in data:
            # если таких таблиц нет
            if row[0] == 0:
                # создаём таблицу для товаров
                with con:
                    con.execute("""
                        CREATE TABLE meetings (
                            id INTEGER PRIMARY KEY,
                            day INTEGER,
                            start_time INTEGER,
                            end_time INTEGER,
                            name TEXT,
                            names TEXT
                        );
                    """)


def delete_data(con):
    with con:
        con.execute('DELETE FROM meetings;')


def check_add_meeting(con, day, start_time, end_time, names):
    # выводим содержимое таблицы с покупками на экран
    with con:
        params = {
            'day': day,
            'start_time': start_time,
            'end_time': end_time
        }
        params.update((f'name{i}', name) for i, name in enumerate(names))
        data = con.execute(
            f"""
            SELECT name FROM meetings 
            WHERE day = :day AND
            (
                (start_time < :start_time AND :start_time < end_time) OR
                (start_time < :end_time AND :end_time < end_time) OR
                
                (:start_time < end_time AND end_time < :end_time) OR
                (:start_time < start_time AND start_time < :end_time)
            ) AND
            name IN ( {', '.join(':name' + str(i) for i in range(len(names)))} )
            """,
            params
        )
        return {row[0] for row in data}


def add_meeting(con, day, start_time, end_time, names):
    # подготавливаем множественный запрос
    sql = 'INSERT INTO meetings (day, start_time, end_time, name, names) values(?, ?, ?, ?, ?)'
    # указываем данные для запроса
    data = list((day, start_time, end_time, name, ' '.join(names)) for name in names)

    # добавляем с помощью множественного запроса все данные сразу
    with con:
        con.executemany(sql, data)


def find_meeting(con, day, name):
    with con:
        return con.execute(
            """
            SELECT start_time, end_time, names
            FROM meetings
            WHERE
                day = ? AND
                name = ?
            ORDER BY
                start_time
            """,
            (day, name)
        )


def parse_str(con, text):
    words = text.split()
    if words[0] == 'APPOINT':
        parse_appoint(con, words)
    parse_print(con, words)


def parse_print(con, words):
    day, name = int(words[1]), words[2]
    rows = find_meeting(con, day, name)
    for start_time, end_time, names in rows:
        print(f'{start_time//60:>02d}:{start_time%60:>02d} {end_time- start_time} {names}')

def parse_appoint(con, words):
    day, time_str, duration, count_people = int(words[1]), words[2], int(words[3]), int(words[4])
    hour, minute = time_str.split(':')
    time_minute = 60 * int(hour) + int(minute)
    names = tuple(words[i] for i in range(5, 5 + count_people))
    start_time, end_time = time_minute, time_minute + duration
    intersection_names = check_add_meeting(con, day, start_time, end_time, names)
    if intersection_names:
        print('FAIL')
        print(' '.join(name for name in names if name in intersection_names))
    else:
        print('OK')
        add_meeting(con, day, time_minute, time_minute + duration, names)


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    con = sl.connect('thecode.db')
    add_table(con)
    delete_data(con)
    for i in range(int(input())):
        parse_str(con, input())


if __name__ == '__main__':
    main()
