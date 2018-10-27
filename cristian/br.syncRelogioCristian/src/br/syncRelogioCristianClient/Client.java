package br.syncRelogioCristianClient;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.io.InputStream;
import java.io.OutputStream;

public class Client {
	
	private long t1, t4;
	private long t2, t3;
	
	public Client() {
		
	}

	public void solicitarHora() {
		try {
			Socket servidor = new Socket("127.0.0.1", 10000);
			
			//Enviar mensagem para o servidor ----------------------------------
            OutputStream saida = servidor.getOutputStream();
            DataOutputStream send = new DataOutputStream(saida);
            //Pegar instante t1
            t1 = System.currentTimeMillis();
            send.writeUTF("Solicitação de atualização de hora de ip: " + servidor.getLocalSocketAddress());
            //-------------------------------------------------------------------
            
            //Receber instantes (t2 e t3) do servidor ----------------------------------------------
            InputStream entrada = servidor.getInputStream();
            DataInputStream recv = new DataInputStream(entrada);
            SimpleDateFormat frmt = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
            t2 = recv.readLong();
            t3 = recv.readLong();
            //-------------------------------------------------------------------
            
            //Pegar instante t4
            t4 = System.currentTimeMillis();
            
            t4 += 557;
            
            //Calcular Tempo de Cristian ----------------------------------------
    		long rtt = ((t4 - t1) + (t3 - t2));
    		
    		Timestamp dataHoraAtt = new Timestamp(System.currentTimeMillis());
    		dataHoraAtt.setTime(t3 + (rtt / 2));
    		long tempoCristian = (t3 + (rtt / 2));
    		//-------------------------------------------------------------------
    		
    		System.out.println("Instante t1: " + t1);
    		System.out.println("Instante t2: " + t2);
    		System.out.println("Instante t3: " + t3);
    		System.out.println("Instante t4: " + t4);
    		System.out.println("Round Trip Time: " + rtt);
    		System.out.println("Tempo de Cristian: " + tempoCristian);
            System.out.println("Hora atualizada: " + frmt.format(dataHoraAtt));
            
		}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	
	public static void main(String[] args) throws IOException {
		Client client = new Client();
		client.solicitarHora();
	}
}