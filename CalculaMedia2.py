soma = 0
cont = 0
FIM = -1

nota = int(input("Entre com a nota: "))
while (nota != FIM):
    soma += nota
    cont += 1
    nota = int(input("Entre com a nota: "))
if (cont > 0):
    media = soma / cont
    print(f"Média = {media: .2f}")
else:
    print("Não há notas")