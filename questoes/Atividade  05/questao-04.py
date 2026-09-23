listaTuplas = [(1,2), (3,4), (5,6)]
listaLista = []

for par in listaTuplas:
    par[1] + 10
    listaLista.append(list(par))

print (listaLista)