def two(vals):
    res = set(vals)
    return list(res)

def main():
    print('Введите количество значений: ', end='')
    i = int(input())
    print('Введите значения: ')
    values = list()
    while i != 0:
        values.append(input())
        i -= 1
    print('Введенные значения: ', values)
    print('Новые значения: ', two(values))


main()
