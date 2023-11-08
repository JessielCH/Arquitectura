/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package compuertalogica;

import javax.swing.JOptionPane;

/**
 *
 * @author BRYAN
 */
public class CompuertaLogica {


    public static void main(String[] args) {
        
        while (true) {
            
            String codigoRFID = JOptionPane.showInputDialog(" \n Ingrese el código RFID del collar del ganado lechero:  \n");

           
            String codigoDeBarras = JOptionPane.showInputDialog("\n Ingrese el código de barras del ganado lechero: \n ");

            
            boolean condicionesCumplidas = codigoRFID.equals(codigoDeBarras);

            
            if (condicionesCumplidas) {
                JOptionPane.showMessageDialog(null, "\n Las condiciones (RFID igual a código de barras) se cumplen. Ganado lechero autorizado.\n ");
            } else {
                JOptionPane.showMessageDialog(null, "\n Error: Los códigos RFID y de barras no son iguales. Acceso denegado.\n");
            }

            
            int opcion = JOptionPane.showConfirmDialog(null, "\n ¿Desea probar otro código de vaca?", "Confirmación", JOptionPane.YES_NO_OPTION);
            if (opcion != JOptionPane.YES_OPTION) {
                
                break;
            }
        }
    }
}





    

