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
