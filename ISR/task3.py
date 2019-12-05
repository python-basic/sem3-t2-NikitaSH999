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
