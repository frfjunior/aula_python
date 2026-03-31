n = int(input("Digite o número de termos da série de Fibonacci: "))

while n <= 0:
    n = int(input("Valor inválido. Digite um inteiro maior que 0: "))

fibonacci = []
a, b = 1, 1

for i in range(n):
    if i == 0 or i == 1:
        fibonacci.append(1)
    else:
        a, b = b, a + b
        fibonacci.append(b)

print("Série de Fibonacci:")
print(*fibonacci, sep=", ")
