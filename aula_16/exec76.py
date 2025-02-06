prods = ('sabão', 2.50, 'arroz', 10.99, 'batata', 5.30)
for i in range(0, len(prods), 2):
    print(f'{prods[i]:.<30}{prods[i+1]:.>10}')