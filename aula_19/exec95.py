def linha1():
    print('-='*30)
def linha2():
    print('-'*60)

jogadores = []

while True:
    linha2()
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

    jogadores.append(jogador.copy())

    continuar = str(input('Continuar? (S/N) ')).strip().upper()
    if continuar == 'N':
        break

linha1()

print(f"cod {'nome':<20} {'gols':<25} {'total'}")
for pos, j in enumerate(jogadores):
    print(f"  {pos} {j['nome']:<20} {str(j['gols por partida']):<25} {j['total de gols']}")

while True:
    while True:
        linha2()
        dJog = int(input("Mostrar dados de qual jogador? "))
        if dJog < len(jogadores) or dJog == 999:
            break
        print(f'ERRO! Não existe jogador com o código {dJog}! Tente novamente')
    if dJog == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dJog]['nome']}:')
    for pos, g in enumerate(jogadores[dJog]['gols por partida']):
        print(f'   No jogo {pos + 1} fez {g} gols.')

print('<< VOLTE SEMPRE >>')
