lista = []
for i in range(0, 5):
    num = int(input('Digite um numero: '))
    if i == 0:
        lista.append(num)
    elif num >= lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)