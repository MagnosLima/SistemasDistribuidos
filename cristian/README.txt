O algoritmo de Cristian se baseia na ideia de um servidor de tempo centralizado
normalmente com receptor UTC.
Sendo assim, os clientes solicitam periodicamente a sincronização de seus relógios
com o relógio do servidor.
Se baseia nos instantes T1 (solicitação do cliente ao servidor), T2 (servidor recebe requisição),
T3 (servidor responde para cliente) e T4 (instante que cliente recebe resposta do servidor).
Através desses instantes é calculado o RTT (Round Trip Time): rtt = ((t4 - t1) + (t3 - t2));
E por fim aplicado o tempo de Cristian que desconta atrasos de comunicação: tempoCristian = (t3 + (rtt / 2));
Essa variação obtida é por fim adicionada ao tempo atual do relógio do cliente.
