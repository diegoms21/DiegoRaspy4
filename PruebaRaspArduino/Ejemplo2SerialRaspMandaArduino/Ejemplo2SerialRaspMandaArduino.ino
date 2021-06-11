void setup(){
  Serial.begin(9600);
  pinMode(8,OUTPUT);
}
void loop(){
  if(Serial.available()>0){ //esperamos a que llegue data
    char c = Serial.read(); //leemos la data
    Serial.print(c); //imprimimos la data
    if(c== 'a'){
      digitalWrite(8,HIGH);     
    }
    else if (c=='b'){
      digitalWrite(8,LOW);
    }
  }
}
