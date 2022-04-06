lista = []
cont = 0
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    cont += 1
    resp = str(input("Voce deseja continuar? [S]/[N]")).upper().strip()
    if resp == "N":
        break
print(f"Voce digitou {cont} vezes")
lista.sort(reverse=True)
print(lista)
print(f"O numero 5 aparece {lista.count(5)} vezes")