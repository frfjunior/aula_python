numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Número inválido! Digite um número positivo menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")

    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    if numero == 0:
        print("0 = 0 unidades")
    elif len(partes) == 3:
        saida_final = f"{partes[0]}, {partes[1]} e {partes[2]}"
        print(f"{numero} = {saida_final}")
    elif len(partes) == 2:
        saida_final = f"{partes[0]} e {partes[1]}"
        print(f"{numero} = {saida_final}")
    elif len(partes) == 1:
        saida_final = partes[0]
        print(f"{numero} = {saida_final}")