num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
  maior = num2
if num2 < menor:
  menor = num2

if num3 > maior:
  maior = num3
if num3 < menor:
  menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")