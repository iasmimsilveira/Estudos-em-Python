import datetime

def entra_data():

    data_ok = False
    while (not data_ok):
        data = input("Entre com a data no formato dd/mm/aaaa: ")
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            data_ok = True
        except:
            print("Data inválida")
    return data

def verifica_data(dia, mes, ano):

    data_ok = True
    if (ano <= 1890):
        print("Ano inválido")
        data_ok = False
    else:
        if ((mes == 4) or (mes == 6) or (mes == 7) or (mes == 11)):
            if ((dia < 1) or (dia > 30)):
                print("Dia inválido")
                data_ok = False
        elif ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 8) or (mes == 10) or (mes == 12)):
            if ((dia < 1) or (dia > 31)):
                print("Dia inválido")
                data_ok = False
        elif (mes == 2):
            if ((ano % 4) == 0):
                if ((dia < 1) or (dia > 29)):
                    print("Dia inválido")
                    data_ok = False
            else:
                if ((dia < 1) or (dia > 28)):
                    print("Dia inválido")
                    data_ok = False
        else:
            print("Mes invalido")
            data_ok = False
    return data_ok

def quebra_data(data):

    data = data.split("/")
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    return dia, mes, ano

if __name__=="__main__":

    data_ok = False
    while (not data_ok):
        data = entra_data()
        dia, mes, ano = quebra_data(data)
        data_ok = verifica_data(dia, mes, ano)
        if (not data_ok):
            print("Entre com uma nova data")
