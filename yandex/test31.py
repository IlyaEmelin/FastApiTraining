import sys

def read_positions(count):
    positions = set()
    for __ in range(count):
        positions.add(tuple(map(int, input().split())))
    return positions

def check_cut_down(
        pos_defend_0,
        pos_empty_0,
        position_defense,
        position_moves,
        n,
        m
    ):
    if (
            pos_defend_0 in position_defense and
            pos_empty_0 not in position_defense and
            pos_empty_0 not in position_moves
    ):
        n_pos, m_pos = pos_defend_0[0], pos_defend_0[1]
        if 1 <= n_pos <= n and 1 <= m_pos <= m:
            n_pos, m_pos = pos_empty_0[0], pos_empty_0[1]
            if 1 <= n_pos <= n and 1 <= m_pos <= m:
                print('Yes')
                return True
    return False



def check_move(position_moves, position_defense, n, m):
    for position_move in position_moves:
        pos_defend = (position_move[0] - 1, position_move[1] - 1)
        pos_empty =  (position_move[0] - 2, position_move[1] - 2)
        if check_cut_down(
                pos_defend,
                pos_empty,
                position_defense,
                position_moves,
                n,
                m
            ):
            break

        pos_defend = (position_move[0] + 1, position_move[1] + 1)
        pos_empty =  (position_move[0] + 2, position_move[1] + 2)
        if check_cut_down(
                pos_defend,
                pos_empty,
                position_defense,
                position_moves,
                n,
                m
            ):
            break

        pos_defend = (position_move[0] - 1, position_move[1] + 1)
        pos_empty =  (position_move[0] - 2, position_move[1] + 2)
        if check_cut_down(
                pos_defend,
                pos_empty,
                position_defense,
                position_moves,
                n,
                m
            ):
            break

        pos_defend = (position_move[0] + 1, position_move[1] - 1)
        pos_empty =  (position_move[0] + 2, position_move[1] - 2)
        if check_cut_down(
                pos_defend,
                pos_empty,
                position_defense,
                position_moves,
                n,
                m
            ):
            break
    else:
        print('No')

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
    n, m = tuple(map(int, input().split()))  # размер доски
    count_white = int(input())  # w
    whites = read_positions(count_white)
    count_black = int(input())  # b
    blacks = read_positions(count_black)
    whose_move = sys.stdin.readline()

    if whose_move == 'white\n':
        check_move(whites, blacks, n, m)
    elif whose_move == 'black\n':
        check_move(blacks, whites, n, m)
    else:
        print('No')


if __name__ == '__main__':
    main()