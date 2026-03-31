while True:
    print("\nLojas Tabajara")
    total = 0
    item = 1

    while True:
        preco = float(input(f"Produto {item}: R$ "))
        if preco == 0:
            break
        while preco < 0:
            preco = float(input("Valor inválido. Digite novamente: R$ "))
        total += preco
        item += 1

    print(f"Total: R$ {total:.2f}")

    dinheiro = float(input("Dinheiro: R$ "))
    while dinheiro < total:
        dinheiro = float(input("Valor insuficiente. Digite o valor pago: R$ "))

    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}")

    continuar = input("Registrar nova compra? (s/n): ").strip().lower()
    if continuar != "s":
        break
