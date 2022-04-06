palavras = ("aprender", "programar", "linguagem", "Python", "requer",
            "muito", "esforco", "e", "sabedoria")

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos:', end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")