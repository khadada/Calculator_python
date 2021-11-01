from art import logo

print(logo)


# TODO: 01 create arithatic function
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def modu(n1, n2):
    return n1 % n2


operators = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
    '%': modu,
}
def calculator():
    num1 = int(input('Entre first number:  '))
    for op in operators:
        print(f'[{op}]')
    operator_chosed = input('Pick one of this operators above: ')
    num2 = int(input('Entre second number:  '))
    result1 = operators[operator_chosed](num1, num2)
    print(f'{num1} {operator_chosed} {num2} = {result1}')
    then = True
    while then:
        print('=' * 50)
        next = input('Do you need to continue type: [y]  or restart again type: [n] ').lower()
        if next == 'n':
            then = False
            calculator() # This is to restart from begin
        elif next == 'y':
            for op in operators:
                print(f'[{op}]')
            pick_next_op = input('Pick one of this operators above: ')
            num3 = int(input('Entre next number:  '))
            result2 = operators[pick_next_op](result1, num3)
            print(f'{result1} {pick_next_op} {num3} = {result2}')
            result1 = result2
calculator()

