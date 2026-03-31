n = int(input("Digite um número inteiro N: "))

while n < 1:
    n = int(input("Valor inválido. Digite N maior ou igual a 1: "))

primos = []
for numero in range(2, n + 1):
    primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        primos.append(numero)

print("Números primos entre 1 e N:")
print(*primos, sep=", ")
