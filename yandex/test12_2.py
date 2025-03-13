import sys
from itertools import islice
from math import sqrt, pow


def get_section(points):
    return list([points[i], points[i+1]] for i in range(len(points) - 1))

def get_result_section(ln, rn, section_ln, section_rn):
    steps = set(ln)
    steps.update(rn)
    steps = sorted(steps)

    result_n = []
    section_ln, section_rn = iter(section_ln), iter(section_rn)
    l_start, l_end, la, lb, lc = next(section_ln)
    r_start, r_end, ra, rb, rc = next(section_rn)
    for start_step, stop_step in get_section(steps):
        if not(l_start <= start_step and stop_step <= l_end):
            l_start, l_end, la, lb, lc = next(section_ln)
        if not(r_start <= start_step and stop_step <= r_end):
            r_start, r_end, ra, rb, rc = next(section_rn)
        result_n.append(
            ((start_step, stop_step), la-ra, lb-rb, lc-rc)
        )
    return result_n

def add_point(start, stop, a, b, c):
    if a != 0:
        try:
            d = sqrt(pow(b, 2) - 4*a*c)
            x1 = (-b + d) / 2 / a
            x2 = (-b - d) / 2 / a
        except ValueError:
            return (start, stop)
        else:
            if x1 == x2:
                return (start, stop)
            else:
                if start < x2 < stop and start < x1 < stop:
                    return (start, x2, x1, stop)
                elif start < x2 < stop:
                    return (start, x2, stop)
                elif start < x1 < stop:
                    return (start, x1, stop)
                return (start, stop)
    elif b != 0:
        x = -b/a
        if start < x < stop:
            return (start, x, stop)
        return (start, stop)
    return (start, stop)

def inner_integral(value, new_a, new_b, new_c):
    return new_a * pow(value, 3) / 3 + new_b * pow(value, 2) / 2 + new_c * value

def integral(result_n):
    result = 0
    for (start, stop), a, b, c in result_n:
        steps = add_point(start, stop, a, b, c)
        result += sum(
            abs(inner_integral(end, a, b, c) - inner_integral(start, a, b, c))
            for start, end in get_section(steps)
        )
    return result

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
    n, m = map(int, input().split())

    ln = list(map(int, islice(input().split(), 0, n + 1)))
    section_ln = get_section(ln)
    for i in range(n):
        section_ln[i].extend(map(int, input().split()))

    rn = list(map(int, islice(input().split(), 0, m + 1)))
    section_rn = get_section(rn)
    for i in range(m):
        section_rn[i].extend(map(int, input().split()))

    result_n = get_result_section(ln, rn, section_ln, section_rn)
    print(integral(result_n))

if __name__ == '__main__':
    main()