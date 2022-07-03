"""
Módulo para cálculos
"""


def identify_number(number):
    """
    Função para identificação dos números
    """
    string = ""
    if (number % 7 == 0 and number % 5 == 0):
        string = "fizzbuzz"
    elif number % 7 == 0:
        string = "buzz"
    elif number % 5 == 0:
        string = "fizz"
    else:
        string = "miss"
    return string
