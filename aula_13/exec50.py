s = 0

for i in range(0, 6):
    num = int(input("Digite um numero: "))
    if (not(num%2)):
        s += num
print(s)