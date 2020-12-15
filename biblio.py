def entra_numero_inteiro(msg):

    num_ok = False
    while (not num_ok):
        try:
            num = int(input(msg))
            num_ok = True
        except:
            print("Erro: número inválido")
    return num

def entra_numero_real(msg):

    num_ok = False
    while (not num_ok):
        try:
            num = float(input(msg))
            num_ok = True
        except:
            print("Erro: número inválido")
    return num

def entra_saldo(msg):

    saldo_ok = False
    while (not saldo_ok):
        saldo = entra_numero_real(msg)
        if (saldo >= 0):
            saldo_ok = True
        else:
            print("Saldo inválido")
    return saldo

def confirmar():

    opcoes = ("s", "S", "n", "N")
    while(True):
        conf = input("Confirma a operação? [s] ou [n]: ")
        if (conf in opcoes):
            if (conf in opcoes[0:1]):
                return True
            else:
                return False
        else: 
            print("Opção inválida")

def debito_credito():

    opcoes = ("d", "D", "c", "C")
    while(True):
        oper = input("Qual a operação desejada? [c]redito ou [d]ebito: ")
        if (oper in opcoes):
                return oper
        else: 
            print("Opção inválida")            