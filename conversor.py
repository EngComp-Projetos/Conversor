# coding=UTF-8
__author__ = 'Edilson'
__author__ = 'Carlos'
__author__ = 'Alan'

import matplotlib.pyplot as plt
import numpy as np

amplitude = 2  # Amplitude do sinal
frequencia = 2  # Frequência do sinal
tempo_duracao = 2  # Tempo  de duração do sinal
frequencia_angular = frequencia * 2 * np.pi  # Frequência angular
tempo = np.linspace(0, tempo_duracao, 2000)
sinal = amplitude * np.cos(frequencia_angular * tempo) ** 2
numero_bits = 16
frequencia_amostragem = 20 * frequencia
periodo_amostragem = 1 / frequencia_amostragem

quantizacao_bits = [amplitude / ((2 ** numero_bits) - 1)]
for i in range(1, numero_bits):
	quantizacao_bits.append(quantizacao_bits[i - 1] * 2)


sinal_amostrado = []
tempo_amostra = []
i = 0
while (i <= tempo_duracao):
	
	amostra = amplitude * np.cos(frequencia_angular * i) ** 2
	soma = 0
	aux = 0
	for n in range(numero_bits - 1, 0, -1):
		aux += quantizacao_bits[n]
		if aux >= amostra:
			aux = soma
		else:
			soma = aux
	sinal_amostrado.append(soma) 
	tempo_amostra.append(i)
	i += periodo_amostragem

f, vetor = plt.subplots(2)
vetor[0].plot(tempo, sinal)
vetor[0].plot(tempo_amostra, sinal_amostrado, drawstyle='steps-post')
vetor[1].stem(tempo_amostra, sinal_amostrado)
plt.show()
