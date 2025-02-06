nums = (int(input("Digite um número: ")),
        int(input("Digite um número: ")), 
        int(input("Digite um número: ")),
        int(input("Digite um número: ")))

print(nums.count(9))
print(nums.index(3))
for num in nums:
    if num%2==0:
        print(num)