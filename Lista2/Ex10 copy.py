import datetime

def verifica_data(data):

    ok = False
    try:
        datetime.datetime.strptime(data, "%d/%m/%Y")
        ok = True
    except:
        print("Erro: formato inválido. Entre com dd/mm/aaaa")    
    return ok

def dividir_data(data):

    data = data.split("/")
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    return dia, mes, ano

data_ok = False
while (not data_ok):
    data = input("Entre com o data: ")
    data_ok = verifica_data(data)

dia, mes, ano = dividir_data(data)
print(dia, mes, ano)
