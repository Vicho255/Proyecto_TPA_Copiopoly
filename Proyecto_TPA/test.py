import random as rd

def dado():
    """
    Genera un numero aleatorio entre el 1 y el 6
    """

    i = rd.randint(1,6)

    return i



while dado() != 0:
    print(dado(),"\n loco")
