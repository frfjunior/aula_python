while True:
    nome = input("Atleta (enter para encerrar): ").strip()
    if nome == "":
        break

    saltos = []
    for i in range(1, 6):
        distancia = float(input(f"{i}º Salto (m): "))
        saltos.append(distancia)

    melhor = max(saltos)
    pior = min(saltos)
    media = (sum(saltos) - melhor - pior) / 3

    print(f"\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor salto: {melhor:.1f} m")
    print(f"Pior salto: {pior:.1f} m")
    print(f"Média dos demais saltos: {media:.1f} m\n")
