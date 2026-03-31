n = int(input("Digite a quantidade de termos da série: "))

while n <= 0:
    n = int(input("Valor inválido. Digite um inteiro maior que 0: "))

soma = 0
denominador = 1

for numerador in range(1, n + 1):
    termo = numerador / denominador
    soma += termo
    print(f"{numerador}/{denominador}", end="")
    if numerador < n:
        print(" + ", end="")
    denominador += 2

print(f"\nSoma da série: {soma:.4f}")
