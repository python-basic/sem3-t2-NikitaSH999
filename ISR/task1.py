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
