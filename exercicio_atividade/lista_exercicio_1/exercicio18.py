tamanho_arquivo_MB = float(input("Insira o tamanho do arquivo em MB: "))

velocidade_internet_MBps = float(input("Insira a velocidade da internet em MB/s: "))

tempo_segundos = tamanho_arquivo_MB / velocidade_internet_MBps

minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

print(f"Tempo estimado: {minutos} min e {segundos} seg")