opcao_a = "F"
opcao_b = "M"

sexo_usuario = input("Insira o sexo (F/M): ").upper()

if sexo_usuario == opcao_a:
        print("O sexo é feminino.")
elif sexo_usuario == opcao_b:
        print("O sexo é masculino.")
else:
        print("Opção inválida. Por favor, insira 'F' para feminino ou 'M' para masculino.")