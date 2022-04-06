lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n in lista:
        print('Numero repetido. Tente novamente')
    else:
        lista.append(n)
    resp = str(input("Voce deseja continuar? [S]/[N]")).upper().strip()
    if resp == "N":
        break

lista.sort()

print(lista)