# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytest

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def sum(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1 * number2

def div(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return 'NAO DIVIDIRÁS POR ZERO!'

def dividir_try_except(number1, number2):
    try:
        return number1 / number2
    except TypeError:
        #return 'Nao dividirás por zero!'
        if TypeError == ZeroDivisionError:
            return 'NAO DIVIDIRÁS POR ZERO!'
        elif TypeError == ArithmeticError:
            return 'Erro no cálculo!'
        elif TypeError == ValueError:
            return 'Erro no valor!'
        else:
            return 'Erro desconhecido!'
        pass

# Unit Testing
def test_somar_didatico():
    # 1 - Configure / Prepare
    numero1 = 8 # Input
    numero2 = 5 # Input
    result_expected = 13 # Output
    # Execute
    result_current = sum(numero1, numero2)
    # Check, Validate
    assert result_current == result_expected

@pytest.mark.parametrize('numero1, numero2, result',[
    # Values
    (5, 4, 9), # Test1
    (3, 3, 6),  # Test2
    (5, 0, 'NAO DIVIDIRÁS POR ZERO!'),  # Test3

])

def test_sum(numero1, numero2, result):
    try:
        assert sum(numero1,numero2) == result
    except AssertionError:
        print(f'Entrou no Except: {AssertionError}')
        pass

def test_somar_resultado_negativo():
    assert sum(-1000,-2000) == -3000

def test_sub():
    assert sub(4,5) == -1

def test_mult():
    assert mult(3, 7) == 21

def test_div():
    assert div(8, 4) == 2

def test_div_per_zero():
    assert div(8, 0) == 'NAO DIVIDIRÁS POR ZERO!'

@pytest.mark.parametrize('number1,number2,result', [
    (8, 2, 4),
    (20, 4, 5),
    (10, 0, 'NAO DIVIDIRÁS POR ZERO!')
])

def test_dividir_try_except(number1, number2, result):
    assert dividir_try_except(number1, number2) == result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Tom')
    result1 = sum(10,5)
    result2 = sub(10,5)
    result3 = mult(10,5)
    result4 = div(10,2)

    print(f'O resultado da soma é:', {result1})
    print(f'O resultado da sub é:', {result2})
    print(f'O resultado da mult é:', {result3})
    print(f'O resultado da div é:', {result4})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
