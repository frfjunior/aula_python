cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00),
}

total = 0
print("Digite o código 0 para encerrar o pedido.")

while True:
    codigo = int(input("Código do item: "))
    if codigo == 0:
        break
    if codigo not in cardapio:
        print("Código inválido.")
        continue

    quantidade = int(input("Quantidade: "))
    while quantidade <= 0:
        quantidade = int(input("Quantidade inválida. Digite novamente: "))

    nome, preco = cardapio[codigo]
    subtotal = preco * quantidade
    total += subtotal
    print(f"{nome} - {quantidade} x R$ {preco:.2f} = R$ {subtotal:.2f}")

print(f"Total geral do pedido: R$ {total:.2f}")
