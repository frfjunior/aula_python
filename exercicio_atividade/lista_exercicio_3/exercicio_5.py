while True:
    while True:
        pop_a = int(input("População inicial de A (maior que 0): "))
        if pop_a > 0:
            break
        print("Valor inválido.")

    while True:
        pop_b = int(input("População inicial de B (maior que 0): "))
        if pop_b > 0:
            break
        print("Valor inválido.")

    while True:
        taxa_a = float(input("Taxa de crescimento de A (%): "))
        if taxa_a > 0:
            taxa_a /= 100
            break
        print("Valor inválido.")

    while True:
        taxa_b = float(input("Taxa de crescimento de B (%): "))
        if taxa_b > 0:
            taxa_b /= 100
            break
        print("Valor inválido.")

    anos = 0
    atual_a = pop_a
    atual_b = pop_b
    while atual_a < atual_b:
        atual_a += atual_a * taxa_a
        atual_b += atual_b * taxa_b
        anos += 1

    print(f"Anos necessários: {anos}")
    print(f"População A final: {int(atual_a)}")
    print(f"População B final: {int(atual_b)}")

    repetir = input("Deseja repetir a operação? (s/n): ").strip().lower()
    if repetir != "s":
        break
