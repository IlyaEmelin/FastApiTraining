import sys
from typing import Dict
import string


def get_key(word):
    gen_word = iter(word)
    shift = ord(next(gen_word))
    return sum(
        map()
        ord(char) - shift if ord(char) - shift >= 0 else ord(char) - shift + len(string.ascii_lowercase)
        for char in gen_word
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
    words = input().split()
    word_dict = {get_key(word): word for word in words}

    encoded_count = int(input())

    for __ in range(encoded_count):
        word = input()
        print(word_dict[get_key(word)])


if __name__ == '__main__':
    main()