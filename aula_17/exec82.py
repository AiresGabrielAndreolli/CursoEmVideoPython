nums = list()
par = list()
impar = list()
while True:
    nums.append(int(input("Digite um número: ")))
    par.append(nums[-1]) if nums[-1] % 2 == 0 else impar.append(nums[-1])
    if str(input("Continuar (S/N) ")).upper() == 'N':
        break
print('A primeira lista é ', *nums)
print('A lista de pares é ', *par)
print('A lista de ímpares é', *impar)