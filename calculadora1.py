from biblio import *

def mostrar_menu():

    fim = False
    while (not fim):
        print("----- Calculadora -----")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Mostrar log")
        print("0 - Sair")
        opcao = entra_numero("Entre com uma opção: ")
        if ((opcao >= 0) and (opcao <= 5)):
            fim = True
        else:
            print("Opção inválida")
    return opcao

def soma(op1, op2, log):
    
    result = op1 + op2
    log.append(str(op1) + " + " + str(op2) + " = " + str(result))
    return result

def subtrai(op1, op2, log):

    result = op1 - op2
    log.append(str(op1) + " - " + str(op2) + " = " + str(result))
    return result

def multiplica(op1, op2, log):

    result = op1 * op2
    log.append(str(op1) + " * " + str(op2) + " = " + str(result))
    return result

def divisao(op1, op2, log):

    if (op2 == 0): 
        result = "Divisão por zero"
    else:
        result = op1 / op2
    log.append(str(op1) + " / " + str(op2) + " = " + str(result))
    return result

def mostrar_log(log):

    for l in log:
        print(l)

def realiza_operacao(opcao, op1, op2, log):

    if (opcao == 1):
        result = soma(op1, op2, log)
    elif (opcao == 2):
        result = subtrai(op1, op2, log)
    elif (opcao == 3):
        result = multiplica(op1, op2, log)
    elif (opcao == 4):
        result = divisao(op1, op2, log)
    return result

OPCOES = (1,2,3,4)
FIM = 0
log = []
opcao = mostrar_menu()
while (opcao != FIM):
    if (opcao in OPCOES):
        op1 = entra_numero("Entre com o op1: ")
        op2 = entra_numero("Entre com o op2: ")
        result = realiza_operacao(opcao, op1, op2, log)
        print("Resultado = ", result)
    else:
        mostrar_log(log)
    opcao = mostrar_menu()
print("Fim da calculadora")    

