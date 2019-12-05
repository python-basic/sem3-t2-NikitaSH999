
Тема 5. Понятие функции, объявление функций
Инвариантная самостоятельная работа:
Задание 1:
"""
Shimko Nikita
IVT 2, group 1
"""
values = ((0, 0), (0, 1), (1, 0), (1, 1))

def head():
    head = '| A | B | C |'
    uhead = '+ ' + '-' * (len(head) - 4) + ' +'
    print(uhead)
    print(head)
    print(uhead)

def logic(val):
    result = (val[0] or val[1]) and (not val[0] or not val[1])
    result = int(result)
    line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result) + ' |'
    print(line)
    print('+', '-' * (len(line)-4), '+')
    return result

def main():
    print('\n4) C = (A∨B)∧(¬A∨¬B)\n')
    head()
    result = dict()
    for i in range(len(values)):
        result.update({'input' + str(values[i]): logic(values[i])})
    print(result)

main()

Задание 2:
"""
Shimko Nikita
IVT 2, group 1
"""
values = ((0, 0), (0, 1), (1, 0), (1, 1))
head = '| A | B | C = (A∨B)∧(¬A∨¬B) |'
line = '|' + '-' * (len(head) - 2) + '|'

def logic(val):
    log_expr =' C =(A∨B)∧(¬A∨¬B) '
    res = (val[0] or val[1]) and (not val[0] or not val[1])
    res = int(res)
    val_line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(res).center(len(log_expr)-1) + ' |'
    print(val_line, line, sep='\n')
    return res

def main():
    print('\nC = (A∨B)∧(¬A∨¬B)', line, head, line, sep='\n')
    result = dict()
    for i in values:
        result.update({'input' + str(i): logic(i)})
    print(result)

main()
Задание 3:
def fib(lst):

    lst21 = lst[len(lst) // 1 - 3 ::-2]
    sum21 = sum(lst21)

    lst11 = lst[1:len(lst) // 2 :2]
    sum11 = sum(lst11)

    return [sum11, sum21]

def main():
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    print(fib(fibs))

main()
