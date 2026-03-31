while True:
    numero = int(input("Digite um inteiro positivo menor que 16: "))
    while numero <= 0 or numero >= 16:
        numero = int(input("Valor inválido. Digite um inteiro entre 1 e 15: "))

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    print(f"Fatorial de {numero}: {fatorial}")

    repetir = input("Deseja calcular outro fatorial? (s/n): ").strip().lower()
    if repetir != "s":
        break
