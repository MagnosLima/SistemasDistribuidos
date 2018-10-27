O algoritmo de Lamport se baseia na ideia de sincronização de tempo lógico.
Ou seja, o que se busca é uma ordenação lógica do tempo de acordo com a sequência
de acontecimentos (eventos) entre os processos.
Uma das questões mais importantes em relação a tal ideia abordada como um problema 
o qual o algoritmo de Lamport propõe solução é de que uma mensagem não pode ser recebida
antes de ser enviada. Por isso, o timestamp de um processo que recebe uma mensagem não pode
ser menor que o timestamp do processo que a enviou (relação happens-before).

Basicamente funciona seguindo as seguintes regras no contador de cada processo:
- Antes de atribuir o timestamp a um evento, pi executa Li := Li + 1
(i.e. incrementa o contador entre eventos sucessivos);
- Quando uma mensagem m é enviada pelo processo p i , a mensagem
recebe o timestamp ts(m) = Li;
- Quando m é recebida por um processo p j , este ajusta o seu contador
Lj := max (Lj , ts(m)) + 1, marcando m com o novo Lj.

