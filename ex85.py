lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º termo: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(lista)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores impares são: {lista[1]}')