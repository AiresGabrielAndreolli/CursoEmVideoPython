from random import randint
from operator import itemgetter

dados = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6)
}
ranking = list()
for k, v in dados.items():
    print(f'O {k} sorteou o número {v}')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for pos, (k, v) in enumerate(ranking, start=1):
    print(f'{pos}º lugar: {k} com o número {v}')
'''
dadosOrdemDes = sorted(dados.items(), key=lambda x: x[1], reverse=True)

for k, v in dados.items():
    print(f'O {k} sorteou o número {v}')

print('\n' + '='*15 + 'Ranking' + '='*15 + '\n' )

for pos, (k, v) in enumerate(dadosOrdemDes, start=1):
    print(f'{pos}º lugar: {k} com o número {v}')
'''