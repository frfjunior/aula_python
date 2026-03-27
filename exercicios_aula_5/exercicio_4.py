for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero == 0:
        print("Processamento interrompido")
        break
else:
    print("Sequência processada com sucesso")