n = int(input("Digite a quantidade de números (N): "))

while n <= 0:
    n = int(input("Valor inválido. Digite N maior que 0: "))

menor = None
maior = None
soma = 0

for i in range(1, n + 1):
    while True:
        numero = float(input(f"Digite o {i}º número (entre 0 e 1000): "))
        if 0 <= numero <= 1000:
            break
        print("Número inválido.")

    soma += numero
    if menor is None or numero < menor:
        menor = numero
    if maior is None or numero > maior:
        maior = numero

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
