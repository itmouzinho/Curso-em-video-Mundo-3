valores = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input("Digite um numero: ")))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi: {maior}, nas posições: ', end='')
for indx, val in enumerate(valores): ## indx e valores
    if val == maior: ## se valor == maior
        print(f'{indx}...', end='') ## print o indice
print(f'\nO menor valor digitado foi: {menor}, nas posicoes: ', end="")
for indx, val in enumerate(valores):
    if val == menor:
        print(f'{indx}...', end='')