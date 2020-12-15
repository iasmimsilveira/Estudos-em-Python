def valida_data(dia, mes, ano):

    result = ""
    if (ano <= 1890):
        result = "Ano inválido"
    else:
        if ((mes == 4) or (mes == 6) or (mes == 7) or (mes == 11)):
            if ((dia < 1) or (dia > 30)):
                result = "Dia inválido"
        elif ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 8) or (mes == 10) or (mes == 12)):
            if ((dia < 1) or (dia > 31)):
                result = "Dia inválido"
        elif (mes == 2):
            if ((ano % 4) == 0):
                if ((dia < 1) or (dia > 29)):
                    result = "Dia inválido"
            else:
                if ((dia < 1) or (dia > 28)):
                    result = "Dia inválido"
        else:
            result = "Mes invalido"
    return result

def entra_data():
    dia = int(input("Entre com o dia: "))
    mes = int(input("Entre com o mes: "))
    ano = int(input("Entre com o ano: "))
    return dia, mes, ano

data_ok = False
while (not data_ok):
    dia, mes, ano = entra_data()
    result = valida_data(dia, mes, ano)
    if (result): 
        print(result)
    else:
        data_ok = True