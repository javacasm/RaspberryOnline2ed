#include <Wire.h>

#define DIRECCION_ESCLAVO 0x09

#define CMD_OFF '0'
#define CMD_ON  '1'

#define PIN_RELE 2


void setup() {
    pinMode(PIN_RELE, OUTPUT);

    Serial.begin(9600); 
    // inicializamos i2c como esclavo con la dirección dada
    Wire.begin(DIRECCION_ESCLAVO);

    // funciones callbacks para la comunicacion i2c 
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    Serial.println("Ready!");
}

void loop() {
    delay(100);
}

// callback para datos recibidos
void receiveData(int byteCount){
    while(Wire.available()) { // Hay datos disponibles
        int comando = Wire.read();
        Serial.print("recibido comando: ");
        Serial.println(comando);
        switch(comando){
        case CMD_ON:
            digitalWrite(PIN_RELE, HIGH); 
            break;
        case CMD_OFF:
            digitalWrite(PIN_RELE, LOW); 
            break;
        default:
            Serial.print("Comando no definido:");
            Serial.println(comando);
        
        }
    }
}
// Cuando nos piden datos enviamos el estado del rele
void sendData(){ 
    int relay_status = digitalRead(PIN_RELE);
    Wire.write(relay_status);
}
