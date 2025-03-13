import sys
from itertools import islice
from collections import OrderedDict

def calc_total_skill(developer_skills, manager_skills):
    count = len(developer_skills)

    sorted_skills = sorted(
        (developer_skill - manager_skill, manager_skill, i + 1)
        for i, (developer_skill, manager_skill) in enumerate(zip(developer_skills, manager_skills))
    )
    total_skill = sum(
        sorted_skill[1] for sorted_skill in sorted_skills[0: count//2]
    ) + sum(
        sorted_skill[0] + sorted_skill[1] for sorted_skill in sorted_skills[count//2: count]
    )
    index_by_skill = {skill[2]: i for i, skill in enumerate(sorted_skills)}
    return total_skill, index_by_skill, sorted_skills

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
    # count = int(input())
    # developer_skills = islice(map(int, input().split()), 0, count)
    # manager_skills = islice(map(int, input().split()), 0, count)
    count = 4
    developer_skills = [7, 15, 3, 4]
    manager_skills = [10, 10, 0, 6]

    total_skill, index_by_skill, sorted_skills = calc_total_skill(developer_skills, manager_skills)
    print('total_skill:', total_skill)
    # count_skill = int(input())
    # map(int, input().split())

    for num_user, type_skill, skill in (1, 1, 4), (4, 1, 6), (2, 2, 10):
        new_num_user = index_by_skill[num_user]
        diff_skill, manager_skill, num_user = sorted_skills[new_num_user]
        diff_skill += skill if type_skill == 1 else -skill

        i = -1
        if type_skill == 1:
            for i in range(new_num_user + 1, len(sorted_skills)):
                if sorted_skills[i][0] > diff_skill:
                    break
        else:
            for i in range(new_num_user - 1, 0, -1):
                if sorted_skills[i][0] < diff_skill:
                    break

        insert_index, del_index = i, new_num_user
        if i > 0 and abs(insert_index - del_index) > 1:
            if insert_index > del_index:
                sorted_skills.insert(insert_index, (diff_skill, manager_skill, num_user))
                sorted_skills.pop(del_index)
            else:
                sorted_skills.pop(del_index)
                sorted_skills.insert(insert_index, (diff_skill, manager_skill, num_user))



if __name__ == '__main__':
    main()