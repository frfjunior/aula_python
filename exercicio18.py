tamanho_arquivo_MB = float(input("Insira o tamanho do arquivo em MB: "))
velocidade_internet_MBps = float(input("Insira a velocidade da internet em MB/s: "))
tempo_download_minutos = (tamanho_arquivo_MB / velocidade_internet_MBps) / 60
print(f"O tempo estimado para o download do arquivo é: ", tempo_download_minutos, "minutos")
