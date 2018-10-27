package br.syncRelogioCristianServer;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server extends Thread {
	private ServerSocket servidor;
   
    public Server() throws Exception {
        servidor = new ServerSocket(10000);
    }

    @Override
    public void run() {
    	System.out.println("Running...");
        while (true) {
            try {	      
                Socket cliente = servidor.accept();
                //Receber solicitação de clientes -----------------------------------------
                DataInputStream recv = new DataInputStream(cliente.getInputStream());
                //Pegar instante t2
                long t2 = System.currentTimeMillis();
                System.out.println(recv.readUTF());
                //-------------------------------------------------------------------------
                
                //Enviar instantes (t2 e t3) para clientes --------------------------------
                DataOutputStream send = new DataOutputStream(cliente.getOutputStream());
            
                //Intervalo de resposta ---------------------------------------------------
                sleep(3526);
                send.writeLong(t2);
                send.writeLong(System.currentTimeMillis());
                
                //-------------------------------------------------------------------------
            
                cliente.close();
                
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }
    }
        
    public static void main(String [] args) throws IOException {
        try {
            Server thread = new Server();
            thread.start();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }	
    }
}
