O algoritmo de Berkeley tem o seu funcionamento baseado nos seguintes passos:
O servidor de tempo pede o tempo aos clientes, faz uma média (tempo total / quantidade de clientes + servidor) dos tempos
e os informa do ajuste necessário individual para que seus tempos atinjam o valor médio.
Se o tempo de um cliente possui variações superiores a uma certa tolerância,
o seu tempo não é usado no cálculo da média.
