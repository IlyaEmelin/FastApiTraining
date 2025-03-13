import sys
from math import sqrt

def discriminant_calk(a, b, c):
    return b**2 - 4 * a * c


def quadratic_calk(a, b, c):
    discriminant = discriminant_calk(a, b, c)
    return (-b + sqrt(discriminant)) / 2 / a


def count_arithmetic(d, a1, sn):
    return quadratic_calk(d, 2*a1 - 1, -2*sn)


def count_book(limit_k, home_m, week_day_d, need_read):
    for i in range(week_day_d, 6):
        home_m -= need_read
        home_m += limit_k
        if home_m <= 0:
            return home_m, need_read
        need_read += 1

    for i in range(max(week_day_d, 6),8):
        home_m -= need_read
        need_read += 1
        if home_m <= 0:
            return home_m, need_read
    return home_m, need_read


def count_day(limit_k, home_m, week_day_d):
    need_read = 1
    while True:
        home_m, need_read = count_book(limit_k, home_m, week_day_d, need_read)
        if home_m == 0:
            return need_read
        if home_m < 0:
            return need_read - 1
        week_day_d = 1


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
    limit_k, home_m, week_day_d = list(map(int, input().split()))
    print(count_day(limit_k, home_m, week_day_d))


if __name__ == '__main__':
    main()