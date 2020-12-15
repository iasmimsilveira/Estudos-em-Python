from biblio import *
import os, sys

class Conta():

    def __init__(self, num, nome, valor):
        self.num = num
        self.nome = nome
        self.saldo = valor

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_saldo(self, valor):
        self.saldo = valor

    def get_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        self.saldo -= valor

    # Sobreescrita = override
    def __str__(self):
        return str(self.num) + " " + self.nome + " " + str(self.saldo)

def mostra_menu():
    OPCOES = (0, 1, 2, 3, 4, 5)

    opcao_ok = False
    while (not opcao_ok):
        print("--- Sistema Bancário ---")
        print("1 - Inclusão")
        print("2 - Alteração")
        print("3 - Exclusão")
        print("4 - Listar")
        print("5 - Movimentar")
        print("0 - Sair")
        opcao = entra_numero_inteiro("Entre com a opção: ")
        if (opcao not in OPCOES):
            print("Opção inválida")
        else:
            opcao_ok = True
    return opcao

def pesquisa_contas(contas, num_conta):

    achou = False
    for conta in contas:
        if (conta.get_num() == num_conta):
            achou = True
    return achou

def pesquisa_contas_index(contas, num_conta):

    index = -1
    for i in range(len(contas)):
        if (contas[i].get_num() == num_conta):
            index = i
    return index

def incluir(contas):
    
    num_conta = entra_numero_inteiro("Entre com o número da conta: ")
    achou = pesquisa_contas(contas, num_conta)
    if (achou):
        print("Erro: conta já existe")
        return
    nome = input("Entre com o nome: ")
    saldo = entra_saldo("Entre com o saldo: ")
    contas.append(Conta(num_conta, nome, saldo))
    return "Conta incluida com sucesso"

def alterar(contas):

    if (not contas):
        print("Não existem contas a serem alteradas")
    num_conta = entra_numero_inteiro("Entre com o número da conta: ")
    index = pesquisa_contas_index(contas, num_conta)
    if (index == -1):
        print("Erro: conta não existe")
        return
    nome = input("Entre com o nome: ")
    saldo = entra_saldo("Entre com o saldo: ")
    contas[index].set_nome(nome)
    contas[index].set_saldo(saldo)
    return "Alteração feita com sucesso"

def excluir(contas):

    if (not contas):
        print("Não existem contas a serem excluidas")
    num_conta = entra_numero_inteiro("Entre com o número da conta: ")
    index = pesquisa_contas_index(contas, num_conta)
    if (index == -1):
        print("Erro: conta não existe")
        return
    if (confirmar()):
        del contas[index]
    return "Exclusão feita com sucesso"

def listar(contas):

    if (not contas):
        print("Não existem contas a serem exibidas")
    for conta in contas:
        print(conta)
    return 

def movimentar(contas):

    if (not contas):
        print("Não existem contas a serem movimentadas")    
    num_conta = entra_numero_inteiro("Entre com o número da conta: ")
    index = pesquisa_contas_index(contas, num_conta)
    if (index == -1):
        print("Erro: conta não existe")
        return    
    oper = debito_credito()
    valor = entra_numero_real("Entre com o valor da operação: ")
    if (oper.upper == "C"):
        contas[index].depositar(valor)
    else:
        contas[index].retirar(valor)

def executa_operacao(contas, opcao):

    if (opcao == 1):
        incluir(contas)
    elif (opcao == 2):
        alterar(contas)
    elif (opcao == 3):
        excluir(contas)
    elif (opcao == 4):
        listar(contas)
    else:
        movimentar(contas)

def le_arquivo(contas):

    with open(NOME_ARQUIVO, "r") as arq:
        for reg in arq.readlines():
            campos = reg.split(";")
            num = int(campos[0])
            nome = campos[1]
            saldo = float(campos[2])
            contas.append(Conta(num, nome, saldo))

def grava_arquivo(contas):

    with open(NOME_ARQUIVO, "w") as arq:
        for conta in contas:
            reg = str(conta.get_num()) + ";" + conta.get_nome() + ";" + str(conta.get_saldo())
            arq.write(reg + "\n")

NOME_ARQUIVO = "contas.txt"
NOME_ARQUIVO = os.path.join(sys.path[0], NOME_ARQUIVO)
FIM = 0
# Lista de contas
contas = []
le_arquivo(contas)
opcao = mostra_menu()
while (opcao != FIM):
    executa_operacao(contas, opcao)
    opcao = mostra_menu()
grava_arquivo(contas)
print("Fim do programa")    