#!/usr/bin/python3

#Cores para formatação
cores = {
            'amarelo':'\033[0;33m',
            'azul':'\033[1;34m',
            'or':'\033[0;30;43m',
            'pb':'\033[7;40m',
            'qq':'\033[0;40m',
            'verde':'\033[0;32m',
            'vrdInverse':'\033[7;30;42m',
            'vrdBack':'\033[30;42m',
            'vermelho':'\033[0;31m',
            'vrmInverse':'\033[7;30;41m',
            'redInverse':'\033[7;30;41m',
            'cls':'\033[m'
        } 

#Informar número de processos
print('{0} {1}LAMPORT{2} {3}'.format(cores['amarelo'], '-'*25, '-'*25, cores['cls']))
ps = int(input('{0}Número de processos:{1} '.format(cores['or'], cores['cls'])))

#Informar número de eventos
eventos = int(input('{0}Número de eventos:{1} '.format(cores['vrdBack'], cores['cls'])))

#Exibe lista de processos
print('Índice de processos: ')
for i in range(ps):
    print('{} - |P{}|'.format(i, i))
print(' {0}{1}'.format(cores['amarelo'], '-'*57))

#Preencher tempos iniciais com 0
times = [[0] for i in range(ps)]

#Contador de eventos
count = 0

#Execução de eventos com ajuste lógico de relógio
while(count < eventos):
    processoSend = int(input('{0}Processo emissor de evento:{1} '.format(cores['or'], cores['cls'])))

    processoRecv = int(input('{0}Processo receptor de evento:{1} '.format(cores['vrdBack'], cores['cls'])))

    #Testa se processo emissor é o mesmo que processo receptor
    if processoSend == processoRecv:
        times[processoSend].append(times[processoSend][-1] + 1)
        #Se a e b são eventos do mesmo processo e a → b, então L(a) < L(b)
        print('Timestamp de evento = {}'.format(times[processoSend][-2]))
        #Mostrando processo e seu respectivo timestamp atual
        print('Relógio de P{0} = {1}'.format((processoSend, times[processoSend][-1])))

    else:
        ''' Antes de atribuir o timestamp a um evento, pi executa Li := Li + 1 
        (incrementa o contador entre eventos sucessivos) '''
        times[processoSend].append(times[processoSend][-1] + 1)
        #Quando uma mensagem m é enviada pelo processo pi, a mensagem recebe o timestamp ts(m) = Li
        print('Timestamp de evento = {}'.format(times[processoSend][-1])) 
        #Mostrando processo e seu respectivo timestamp atual
        print('Relógio de P%s = %s' % (processoSend, times[processoSend][-1]))

        ''' Testa se timestamp de envio é maior do que timestamp que recebe, se for,
        incrementa +1 no relógio do processo receptor em relação ao timestamp do processo que envia. '''
        if times[processoSend][-1] > times[processoRecv][-1]:
            times[processoRecv].append(times[processoSend][-1] + 1)
            #Mostrando processo e seu respectivo timestamp atual
            print('Relógio de P%s = %s' % (processoRecv, times[processoRecv][-1]))
        else:
            ''' Quando m é recebida por um processo pj, este ajusta o seu contador 
            Lj := max (Lj, ts(m)) + 1, marcando m com o novo Lj '''
            times[processoRecv].append(times[processoRecv][-1] + 1)
            #Mostrando processo e seu respectivo timestamp atual
            print("Relógio de P%s = %s" % (processoRecv, times[processoRecv][-1]))

    #Incrementa contador de eventos
    count = count + 1

#Mostrar relógios ajustados de acordo com a execução dos eventos
p = 0
print('\n{}Registro de relógios de processos na execução de eventos:{}'.format(cores['azul'], cores['cls']))
for r in times:
    print("\033[1mRelógio de P{}: {}\033[m".format(p, r))
    #print(r)
    p = p + 1
