numero = int(input("Digite um número inteiro para calcular o fatorial: "))

while numero < 0:
    numero = int(input("Valor inválido. Digite um inteiro não negativo: "))

fatorial = 1
conta = []
for i in range(numero, 0, -1):
    fatorial *= i
    conta.append(str(i))

if numero == 0:
    conta.append("1")

print(f"{numero}! = {' . '.join(conta)} = {fatorial}")
