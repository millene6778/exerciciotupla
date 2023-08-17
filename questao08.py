def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

tempos_corredores = {}
for i in range(6):
    nome_corredor = input(f"Digite o nome do corredor {i+1}: ")
    tempos = []
    for volta in range(1, 11):
        tempo = float(input(f"Digite o tempo da volta {volta} para {nome_corredor} (segundos): "))
        tempos.append(tempo)
    tempos_corredores[nome_corredor] = tempos

melhor_volta = float('inf')
melhor_corredor = ""
melhor_volta_numero = 0

for corredor, tempos in tempos_corredores.items():
    melhor_tempo = min(tempos)
    if melhor_tempo < melhor_volta:
        melhor_volta = melhor_tempo
        melhor_corredor = corredor
        melhor_volta_numero = tempos.index(melhor_tempo) + 1

classificacao_final = sorted(tempos_corredores.keys(), key=lambda corredor: calcular_media_tempos(tempos_corredores[corredor]))
print(f"A melhor volta foi de {melhor_corredor} na volta {melhor_volta_numero} com tempo de {melhor_volta:.2f} segundos.")

print("\nClassificação final:")
posicao = 1
for corredor in classificacao_final:
    media_tempo = calcular_media_tempos(tempos_corredores[corredor])
    print(f"{posicao}º lugar: {corredor} - Média de tempo: {media_tempo:.2f} segundos")
    posicao += 1
