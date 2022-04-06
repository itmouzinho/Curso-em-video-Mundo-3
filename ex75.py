x = (int(input("Digite um valor: ")),
int(input("Digite um valor: ")),
int(input("Digite um valor: ")),
int(input("Digite um valor: ")))

print("Os valores digitados foram: {}".format(x))

print(f'O maior valor digitado foi {max(x)}')
print(f'O menor valor digitado foi {min(x)}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O valor 3 apareceu na {x.index(3) + 1} posicao')
else:
    print("O valor nao esta na tupla")
for i in x:
    if i % 2 == 0:
        print(i)