def linha():
    print('-='*18)

nome = str(input("Nome: "))
partidas = int(input("Partidas Jogadas: "))

golsPorPartida = []

for i in range(1, partidas+1):
    golsPorPartida.append(int(input(f"Gols na {i}º partida: ")))

jogador = {
    'nome' : nome,
    'partidas jogadas' : partidas,
    'gols por partida' : golsPorPartida,
    'total de gols' : sum(golsPorPartida)
}
linha()
print(jogador)
linha()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
linha()
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas jogadas"]} partidas.')
for pos, v in enumerate(jogador['gols por partida']):
    print(f'\t => Na partida {pos+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')