numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

inicio = min(numero1, numero2)
fim = max(numero1, numero2)
soma = 0

print("Números no intervalo:")
for numero in range(inicio, fim + 1):
    print(numero)
    soma += numero

print(f"Soma dos números: {soma}")
