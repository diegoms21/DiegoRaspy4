#include <dht11.h> #falta agregar esta libreria al raspberry
dht11 dht;
void setup(){
  Serial.begin(9600);
}
void loop(){
  dht.read(2);
  Serial.print(dht.temperature);
  Serial.print(",");
  Serial.print(dht.humidity);
  delay(500);
}



