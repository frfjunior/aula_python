numero = int(input("Fatorial de: "))

while numero < 0:
    numero = int(input("Valor inválido. Digite um inteiro não negativo: "))

fatorial = 1
partes = []
for i in range(numero, 0, -1):
    fatorial *= i
    partes.append(str(i))

if numero == 0:
    partes.append("1")

print(f"{numero}! = {' . '.join(partes)} = {fatorial}")
