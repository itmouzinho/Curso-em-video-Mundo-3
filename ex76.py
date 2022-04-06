listagem = ('Lapis', 2,
            'Borracha', 15,
            'Computador', 3560,
            'Caderno', 3.5,
            'Estojo', 7)

print("-" * 30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 30)
for i in range(0, len(listagem)): # i representa a posicao do item
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='') #< representa alinhado a esquerda e .. é os pontos seguintes
    else:
        print(f'R${listagem[i]:>8.2f}')