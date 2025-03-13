import sys
from typing import Dict
import string


def get_codding_dict(shift) -> Dict[str, str]:
    count = len(string.ascii_lowercase)
    start = ord(string.ascii_lowercase[0])
    return {char: chr((ord(char) - start + shift) % count + start) for char in string.ascii_lowercase}


def get_word_dict(words):
    word_dict = {}
    for word in words:
        word_dict.setdefault(len(word), set()).add(word)
    return word_dict


def get_codding_shift(encoded_char, char):
    shift = ord(encoded_char) - ord(char)
    if shift < 0:
        return len(string.ascii_lowercase) + shift
    return shift


def get_encoding_word(word_dict, encoded_word):
    len_encoded_word = len(encoded_word)
    for word in word_dict[len_encoded_word]:
        char_iter, encoded_char_iter = iter(word), iter(encoded_word)
        shift = get_codding_shift(next(encoded_char_iter), next(char_iter))
        if all(
                shift == get_codding_shift(encoded_char, char)
                for encoded_char, char in zip(encoded_char_iter, char_iter)
        ):
            return word


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
    word_dict = get_word_dict(words)

    encoded_count = int(input())
    encoded_words = list(input() for __ in range(encoded_count))

    for encoded_word in encoded_words:
        print(get_encoding_word(word_dict, encoded_word))


if __name__ == '__main__':
    main()