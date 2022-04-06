import moeda

p = float(input('Digite um valor: '))
while True:
    resp = input(print('Voce deseja incorporar alguma taxa? [S/N]'))
    if resp not in "sn".strip():
        print("Resposta invalida")
        resp = input(print('Voce deseja incorporar alguma taxa? [S/N]'))
    if resp == "s".strip():
        taxa = int(input(print('Qual o valor da taxa?')))
        break
    else:
        taxa = 0
        break

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando uma taxa de {taxa}% de {moeda.moeda(p)}, temos {moeda.aumentar(p, taxa, True)}')
print(f'Diminuindo uma taxa de {taxa}% de {moeda.moeda(p)}, temos {moeda.diminuir(p, taxa, True)}')