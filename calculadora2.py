from biblio import *

class Calculadora():

    def __init__(self):
        self.log = []

    def soma(self, op1, op2):
        
        result = op1 + op2
        self.log.append(str(op1) + " + " + str(op2) + " = " + str(result))
        return result

    def subtrai(self, op1, op2):

        result = op1 - op2
        self.log.append(str(op1) + " - " + str(op2) + " = " + str(result))
        return result

    def multiplica(self, op1, op2):

        result = op1 * op2
        self.log.append(str(op1) + " * " + str(op2) + " = " + str(result))
        return result

    def divisao(self, op1, op2):

        if (op2 == 0): 
            result = "Divisão por zero"
        else:
            result = op1 / op2
        self.log.append(str(op1) + " / " + str(op2) + " = " + str(result))
        return result

    def get_log(self):

        return self.log

class CalculadoraAvancada(Calculadora):

    def __init__(self):
        super().__init__()

    def exp(self, op1, op2):

        result = op1 ** op2
        self.log.append(str(op1) + " ^ " + str(op2) + " = " + str(result))
        return result

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

def realiza_operacao(opcao, op1, op2, calc):

    if (opcao == 1):
        result = calc.soma(op1, op2)
    elif (opcao == 2):
        result = calc.subtrai(op1, op2)
    elif (opcao == 3):
        result = calc.multiplica(op1, op2)
    elif (opcao == 4):
        result = calc.divisao(op1, op2)
    return result


ca = CalculadoraAvancada()
result = ca.exp(2, 20)
print(result)

"""
OPCOES = (1,2,3,4)
FIM = 0

opcao = mostrar_menu()
while (opcao != FIM):
    if (opcao in OPCOES):
        op1 = entra_numero("Entre com o op1: ")
        op2 = entra_numero("Entre com o op2: ")
        result = realiza_operacao(opcao, op1, op2, calc)
        print("Resultado = ", result)
    else:
        log = calc.get_log()
        print(log)
    opcao = mostrar_menu()
print("Fim da calculadora")
"""