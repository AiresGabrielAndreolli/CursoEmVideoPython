filme = {

    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'Harisson Ford'

}

print(filme.values())
del filme['diretor']
print(filme.values())
filme['diretor'] = 'George Lucas'
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')


locadora = [
    {'titulo':'Star Wars', 'ano':1977, 'diretor':'Harisson Ford'},
    {'titulo':'Avengers', 'ano':2012, 'diretor':'Joss Whedon'},           
    {'titulo':'Matrix', 'ano':1999, 'diretor':'Whachowski'}
]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])


pessoas = {

    'nome':'Gabriel',
    'sexo':'Masculino',
    'idade':16

}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #usar "nome" ao inves de 'nome'
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['nome'] = 'Gustavo'
pessoas['Peso'] = 98.5

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {
    'uf':'Rio de janeiro',
    'sigla':'RJ'
}
estado2 = {
    'uf':'São Paulo',
    'sigla':'SP'
}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

del brasil

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())  #cria copia
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
for e in brasil:
    for k in e.keys():
        print(k)