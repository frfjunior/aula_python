peso_maximo = float(50)
valor_multa = float(4)
peso_de_peixes = float(input("Insira o peso dos peixes em kg: "))

def verificao_peso(peso_de_peixes, peso_maximo, valor_multa):
    if peso_de_peixes > peso_maximo:
        excesso = peso_de_peixes - peso_maximo
        multa = excesso * valor_multa
        print("O peso dos peixes excede o limite permitido. O excesso é de ", excesso, " kg.")
        print("A multa a ser paga é de R$ ", multa)
    else:
        print("O peso dos peixes está dentro do limite permitido. Não há multa.")

verificao_peso(peso_de_peixes, peso_maximo, valor_multa)