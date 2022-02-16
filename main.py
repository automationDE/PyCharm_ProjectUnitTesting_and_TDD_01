# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytest

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

@pytest.mark.parametrize('numero1,numero2,result', [
    # Values
    (5, 4, 9), # test1
    (3, 2, 5), # test2
    (10, 6, 16), # test3
])
def test_sum(numero1, numero2, result):
    assert sum(numero1,numero2) == result

#def test_sum_compact():
#    assert sum(10,5) == 15

#def test_sum_result():
#    assert sum(-1000,-2000) == -3000

#def test_sub():
#    assert sub(4,5) == -1

def sum(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1 * number2

def div(number1, number2):
    return number1 / number2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Tom')
    result1 = sum(10,5)
    result2 = sub(10,5)
    result3 = mult(10,5)
    result4 = div(10,0)

    print(f'O resultado da soma é:', {result1})
    print(f'O resultado da sub é:', {result2})
    print(f'O resultado da mult é:', {result3})
    print(f'O resultado da div é:', {result4})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
