import sys
import string

def load_count(text):
    i, result, num = 0, [], ''
    while i<len(text):
        char = text[i]
        if char in string.digits:
            num += char
        else:
            if num == '':
                result.append(1)
            else:
                result.append(int(num))
                num = ''
        i += 1
    return result

def len_text(array, l, r):
    l -= 1
    i = 0
    while l != 0:
        count = array[i]
        i += 1
        if count == 1:
            l -= count
            r -= count
        else:
            diff_l = l - count
            if diff_l > 0:
                l -= count
                r -= count
            else:
                l = 0
                diff_r = r - count
                if diff_r > 0:
                    r -= count
                    yield -diff_l
                else:
                    r = 0
                    yield -diff_l + diff_r
    while r!= 0:
        count = array[i]
        i += 1
        if count == 1:
            r -= count
            yield count
        else:
            diff_r = r - count
            if diff_r >= 0:
                r -= count
                yield count
            else:
                r = 0
                yield count+diff_r


def sum_text(array_len):
    result = 0
    for count in array_len:
        if count in (0, 1, 2):
            result += count
        else:
            result += len(str(count)) + 1
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
    # TODO: ошибка в задание
    arrays_key = load_count(input())
    for __ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        print(sum_text(len_text(arrays_key, l, r)))

    # arrays_key = load_count('a2bc3a')
    # print(len_text(arrays_key, 1, 7))  # 6  [1, 2, 1, 3]
    # print(len_text(arrays_key, 5, 7))  # 2  [3]
    # print(len_text(arrays_key, 1, 2))  # 2  [1, 1]
    # print(len_text(arrays_key, 3, 5))  # 3  [1, 1, 1]
    # print(sum_text(len_text(arrays_key, 4, 4)))  # 1  [0, 1]


if __name__ == '__main__':
    main()