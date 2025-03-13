import sys
from itertools import islice


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
    count = int(input())
    numbers = sorted(islice(map(int, input().split()), 0, count))

    count_num, num = 1, numbers[0]
    max_count_num, max_num = 0, numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            count_num += 1
        else:
            if max_count_num <= count_num:
                max_count_num, max_num = count_num, num
            num, count_num = numbers[i + 1], 1
    if count_num >= max_count_num:
        max_num = num
    print(max_num)

if __name__ == '__main__':
    main()