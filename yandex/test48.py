import sys
from itertools import islice


MAX_DISTANCE = pow(2, 30) + 1


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

    product_group = {}
    for __ in range(count):
        args = tuple(map(int, input().split()))
        product_group[args[0]] = args[1]

    data = list(map(
        lambda product: product_group[product],
        islice(map(int, input().split()), 0, count)
    ))
    category_dict = {}
    distance_category = []
    for i, category in enumerate(data):
        index = category_dict.get(category, None)
        if index is None:
            distance_category.append(MAX_DISTANCE)
        else:
            distance_category.append(i - index)
        category_dict[category] = i

    if all(distance == MAX_DISTANCE for distance in distance_category):
        print(len(distance_category))
    else:
        print(min(distance_category))


if __name__ == '__main__':
    main()