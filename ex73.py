times = ("Flamengo", "Palmeiras", "Santos", "Sao Paulo", "Corintians", "Internacional", "Gremio", "Bahia", "Athletico-PR",
         "Goias", "Vasco da gama", "Atletico", "Botafogo", "Fortaleza", "Ceara SC", "Fluminense", "Cruzeiro", "CSA",
         "Chapecoense", "Avai")


print("Os 5 primeiros colocados do brasileirao são: {}".format(times[:5]))

print("Os 5 ultimos sao: {}".format(times[16:20]))

print("Times em ordem alfabetica sao: {}".format(sorted(times)))

print("Chepcoense esta na {} posicao".format(times.index("Chapecoense") + 1))