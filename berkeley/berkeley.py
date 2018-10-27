#!/usr/bin/python3
from time import sleep

#Dicionarios times (tempos considerados para cálculo da média) e times2 (desconsiderados para cálculo da média)
times = {}
times2 = {}

#Cores para formatação
cores = {
			'amarelo':'\033[0;33m',
			'azul':'\033[0;34m',
			'or':'\033[0;30;43m',
			'pb':'\033[7;40m',
			'qq':'\033[0;40m',
			'verde':'\033[0;32m',
			'vrdInverse':'\033[7;30;42m',
			'vermelho':'\033[0;31m',
			'vrmInverse':'\033[7;30;41m',
			'redInverse':'\033[7;30;41m',
			'cls':'\033[m'
		}

#Entrada de número de clientes
print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))
n = int(input('{0} Número de clientes:{1} '.format(cores['or'], cores['cls'])))

#Entrada de tempo do servidor
print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))
hora = input('{0} Hora do servidor (formato HH:MM):{1} '.format(cores['qq'], cores['cls'])).split(':')                                         
h = int(hora[0])
m = int(hora[1])
tmServer = h*60 + m

#Adicionar tempo do servidor no dicionário de tempos para cálculo de média
times[0] = tmServer

#Pegar tempo dos clientes
for i in range(n):
	print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))
	hora = input('{0} Hora do cliente {1} (formato HH:MM):{2} '.format(cores['pb'], (i + 1), cores['cls'])).split(':')                              
	h = int(hora[0])
	m = int(hora[1])
	#Armazenando tempo em minutos
	tm = h*60 + m

	#Media relativa
	avg = sum(times.values()) / (len(times))

	#Testa se tempo a ser adicionado possui diferença (superior ou inferior) a 40 minutos
	if(abs(tm - avg) < 40):
		times[i + 1] = tm
	else:
		print('{0} Variação superior a 40 minutos acima da média, cliente ignorado, offset de: {1} Min. {2}'.format(cores['redInverse'], abs(tm - avg), cores['cls']))
		times2[i + 1] = tm

#Media absoluta
avg = sum(times.values()) / (len(times))

#Estatísticas
print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))
print('\033[3mTempo total considerado para média: {} Min.\033[m'.format(sum(times.values())))
print('\033[3mNúmero de relógios considerados para média: {}\033[m'.format(len(times)))
print('\033[3mMédia: {0}/{1} = {2} Min.\033[m'.format(sum(times.values()), len(times), avg))


print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))

#Concatenar dicionarios para iterar no final calculando ajustes de tempo de cada nó
times.update(times2)

#Ajuste para servidor
ajusteServer = avg - times[0]
nh = int((times[0] + ajusteServer)//60)
nm = int((times[0] + ajusteServer)%60)

if avg > 0:
	cor = cores['vrdInverse']
else:
	cor = cores['vrmInverse']

sleep(1)

#Mostrar ajuste de servidor
print('Ajustar servidor em: {0}\t {1:>+6} Min. --> {2:0>2}:{3:0>2} {4}'.format(cor, ajusteServer, nh, nm, cores['cls']))        

#Ajustes para clientes
for i in range(len(times)):
	i = i + 1

	if i in times:
		ajuste = avg - times[i]
		#Mostar ajustes de clientes
		if ajuste > 0:
			print('Ajustar cliente {0} em:{1}\t{2:>+7} Min. --> {3:0>2}:{4:0>2} {5}'.format(i, cores['vrdInverse'], ajuste, nh, nm, cores['cls']))
		else:
			print('Ajustar cliente {0} em:{1}\t{2:>7} Min. --> {3:0>2}:{4:0>2} {5}'.format(i, cores['vrmInverse'], ajuste, nh, nm, cores['cls']))
print('{0}{1}{2}'.format(cores['azul'], '-'*90, cores['cls']))
	  