lista = []
aux = []
i = 0
maior = menor = 0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]
    lista.append(aux[:])
    aux.clear()
    i += 1
    resp = ' '
    resp = str(input('Deseja continuar? [S]/[N]')).upper().strip()
    if resp == "N":
        break
print(lista)
print(f'Foram cadastradas {i} pessoas')
print(f'O maior peso foi de {maior}kgs ', end='')
for p in lista:
    if p[1] == maior:
        print(f'da pessoa: {p[0]}')
print(f'O menor peso foi de {menor}kgs', end='')
for p in lista:
    if p[1] == menor:
        print(f'da pessoa: {p[0]}')

