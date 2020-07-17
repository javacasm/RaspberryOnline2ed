#define VERSION "V:1.0"

#define SEPARADOR_SERIE ";"
#define PERIODO_LECTURA_SENSORES 1000

#define CMD_RETURN_ERROR -1
#define CMD_RETURN_OK     0
#define CMD_RETURN_UNKOWN 1

#define CMD_PIN_HIGH   'H'
#define CMD_PIN_LOW    'L'

int sensor1,sensor2,sensor3;

int mostrarDatosSerie() {
  Serial.print(sensor1);
  Serial.print(F(SEPARADOR_SERIE));
  Serial.print(sensor2);
  Serial.print(F(SEPARADOR_SERIE));
  Serial.print(sensor3);

  Serial.println();
  return CMD_RETURN_OK;
}

int leerPuertoSerie(){
  if (Serial.available() > 0) {
    int incomingByte = Serial.read();
    if (incomingByte == CMD_PIN_HIGH) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    if (incomingByte == CMD_PIN_LOW) {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
  
}

void setup() {
  pinMode(LED_BUILTIN,OUTPUT);
  Serial.begin(9600);
}
int  leerSensores() {
  sensor1 = analogRead(A0);
  sensor2 = analogRead(A1);
  sensor3 = analogRead(A2);
  return CMD_RETURN_OK;
}

long tiempoUltimoDato;

void loop() {
long tiempoActual = millis();

  leerPuertoSerie();

  if (tiempoActual - tiempoUltimoDato > PERIODO_LECTURA_SENSORES ) {
    leerSensores();
    mostrarDatosSerie();
    tiempoUltimoDato = tiempoActual;
  }

}
