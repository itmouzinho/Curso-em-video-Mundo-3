def aumentar(preco=0, taxa=0, formato = False):
    resp = preco * (1 + taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preco = 0, taxa=0, formato = False):
    resp = preco * (1 - taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preco = 0, formato = False):
    resp = preco * 2
    return resp if formato is False else moeda(resp)


def metade(preco = 0, formato = False):
    resp = preco / 2
    return resp if format is False else moeda(resp)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')