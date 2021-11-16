idades = [39, 30, 27, 18]

type(idades)

len(idades)

idades[0]

print(idades)

idades.append(15)

print(idades)

## Modulo 1 - Aula 2 - List Comprehension

29 in idades

idades.insert(0, 20)

idades.extend([27, 19])

idades_no_ano_que_vem = [(idade + 1) for idade in idades]

[(idade) for idade in idades if idade > 21]


## Modulo 1 - Aula 3 - Mutabilidade de Listas

def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13)


idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
idades
