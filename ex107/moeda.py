def aumentar(preco, taxa):
    resp = preco * (1 + taxa/100)
    return resp

def diminuir(preco, taxa):
    resp = preco * (1 - taxa/100)
    return resp

def dobro(preco):
    resp = preco * 2
    return resp

def metade(preco):
    resp = preco / 2
    return resp

