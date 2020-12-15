
def verifica_primo(num):

    eprimo = True
    for divisor in range(2, num):
        if ((num % divisor) == 0):
            eprimo = False
            break
    return eprimo

def entra_numero():

    num_ok = False
    while (not num_ok):
        try:
            num = int(input("Entre com um número: "))
            num_ok = True
        except:
            print("Erro: número inválido")
    return num


num = entra_numero()
if (verifica_primo(num)):
    print(num, "é primo")
else:
    print(num, "não é primo")
