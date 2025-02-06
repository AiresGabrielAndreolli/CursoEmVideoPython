from random import sample

jogos = []


qtdJogos = int(input("Quantos jogos você quer jogar? "))
for i in range(0, qtdJogos):
    jogos.append(sample(range(1, 61), k = 6)) #se der errado volta pra choices 

print(f'Minha sugestão de jogos para você é:')
for i in range(0, len(jogos)):
    print(*jogos[i])
print('Boa Sorte!')