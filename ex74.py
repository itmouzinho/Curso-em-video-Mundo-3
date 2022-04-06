from random import randint

sorteado = (randint(1, 999), randint(1, 199), randint(1, 999), randint(1, 999), randint(1, 99))
print("Os valores sorteados foram: ")
for i in sorteado:
    print(i)
print("o maior valor foi: {}".format(max(sorteado)))
print("O menor valor foi: {}".format(min(sorteado)))

