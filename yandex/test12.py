import sys
from itertools import islice
from math import sqrt, pow


def get_section(points):
    return (
        (start_p, stop_p) for start_p, stop_p in zip(
            map(
                lambda i: points[i],
                range(0, len(points), 2)
            ),
            map(
                lambda i: points[i],
                range(1, len(points), 2)
            )
        )
    )

def get_result_section(ln, rn):
    ln = get_section(ln)
    rn = get_section(rn)
    l_start, l_end = next(ln)
    r_start, r_end = next(rn)
    result_n = list()
    while True:
        if r_start > l_end:
            for l_start, l_end in ln:
                if r_start > l_end:
                    break

        if l_start > r_end:
            for r_start, r_end in rn:
                if l_start > r_end:
                    break

        if r_start < l_end and l_start < r_end:
            result_n.append(
                (max(l_start, r_start), min(l_end, r_end))
            )

            try:
                l_start, l_end = next(ln)
            except StopIteration:
                try:
                    r_start, r_end = next(rn)
                except StopIteration:
                    break
        else:
            break

    return result_n

def add_point(result_n, na, nb, nc):
    if na != 0:
        try:
            d = sqrt(pow(nb, 2) - 4*na*nc)
            x1 = (-nb + d) / 2 / na
            x2 = (-nb - d) / 2 / na
        except ValueError:
            pass
        else:
            result_new = []
            for n_start, n_end in result_n:
                added = False
                if n_start < x1 < n_end:
                    result_new.append((n_start, x1))
                    result_new.append((x1, n_end))
                    added = True
                if n_start < x2 < n_end:
                    result_new.append((n_start, x2))
                    result_new.append((x2, n_end))
                    added = True
                if added is False:
                    result_new.append((n_start, n_end))
            return result_new
    elif na != 0:
        x = -nb/na
        result_new = []
        for n_start, n_end in result_n:
            if n_start < x < n_end:
                result_new.append((n_start, x))
                result_new.append((x, n_end))
        return result_new
    return result_n

def inner_integral(value, new_a, new_b, new_c):
    return new_a * pow(value, 3) / 3 + new_b * pow(value, 2) / 2 + new_c * value

def integral(result_n, new_a, new_b, new_c):
    return sum(
        abs(inner_integral(n_end, new_a, new_b, new_c) - inner_integral(n_start, new_a, new_b, new_c))
        for n_start, n_end in result_n
    )

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
    la, lb, lc = map(int, input().split())

    rn = list(map(int, islice(input().split(), 0, m + 1)))
    ra, rb, rc = map(int, input().split())

    result_n = get_result_section(ln, rn)
    new_a, new_b, new_c = la - ra, lb - rb, lc - rc
    result_n = add_point(result_n, new_a, new_b, new_c)
    print(integral(result_n, new_a, new_b, new_c))

if __name__ == '__main__':
    main()