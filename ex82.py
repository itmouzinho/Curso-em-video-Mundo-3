lista = []
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    resp = str(input(("Voce seja continuar? [S]/[N]"))).upper().strip()
    if resp == "N":
        break
for indx, val in enumerate(lista):
    if val % 2 == 0:
        listaPar.append(val)
    else:
        listaImpar.append(val)
print(lista)
print(listaImpar)
print(listaPar)
