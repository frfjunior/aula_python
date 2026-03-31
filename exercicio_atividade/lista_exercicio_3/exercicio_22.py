numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)

    if len(divisores) == 0:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
        print("Divisível por:", ", ".join(map(str, divisores)))
