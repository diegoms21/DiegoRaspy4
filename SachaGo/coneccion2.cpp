#include <Arduino.h>

const int SW_llave = 13 ; //rele 14
const int SW_derecha = 12; //rele 2
const int SW_izquierda = 11 ; //rele 3
const int SW_ledInf = 10; //rele 4
const int SW_ledSup = 9 ; //rele 5
const int SW_luzAlta = 8; //rele 6
const int SW_claxon = 7; //rele 7
const int SW_velocidad1 = 6; //rele 8
const int SW_velocidad2 = 5; //rele 9
//const int SW_intermitente = 4; //rele 10

const int Bit1 = 4;
const int Bit2 = 3;
const int Bit3 = 2;

void set_valores(){
digitalWrite(SW_derecha,HIGH);
digitalWrite(SW_izquierda,HIGH);
digitalWrite(SW_ledSup,HIGH);
digitalWrite(SW_ledInf,HIGH);
digitalWrite(SW_luzAlta,HIGH);
digitalWrite(SW_llave,HIGH);
digitalWrite(SW_claxon,HIGH);
digitalWrite(SW_velocidad1,HIGH);
digitalWrite(SW_velocidad2,HIGH);
}


void setup() {
Serial.begin(9600);
pinMode(SW_derecha,OUTPUT);
pinMode(SW_izquierda,OUTPUT);
pinMode(SW_ledSup,OUTPUT);
pinMode(SW_ledInf,OUTPUT);
pinMode(SW_luzAlta,OUTPUT);
pinMode(SW_llave,OUTPUT);
pinMode(SW_claxon,OUTPUT);
pinMode(SW_velocidad1,OUTPUT);
pinMode(SW_velocidad2,OUTPUT);

pinMode(Bit1,OUTPUT);
pinMode(Bit2,OUTPUT);
pinMode(Bit3,OUTPUT);

set_valores();
}

void loop() {
  
  if (Serial.available() > 0){
  char rd1 = Serial.read();  
  if (rd1 == 'a'){
  int flag1 = 1;
  digitalWrite(SW_llave,LOW);
  Serial.println(rd1);
    while (flag1 == 1) { //RELE 6 LLAVE
      
      if (Serial.available() > 0){
      char rd = Serial.read();
        if (rd == 'b'){ //APAGAR LLAVE
        set_valores(); //pone el HIGH a todos
        Serial.println(rd1);
        flag1 = 0;
        }
         else if (rd == 'c'){ //DERECHA
           digitalWrite(SW_derecha,LOW);
           digitalWrite(SW_izquierda,HIGH);
           Serial.println(rd);
          }
          else if (rd == 'd'){
          digitalWrite(SW_derecha,HIGH);
          digitalWrite(SW_izquierda,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'e'){ //IZQUIERDA
          digitalWrite(SW_izquierda,LOW);
          digitalWrite(SW_derecha,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'f'){
          digitalWrite(SW_izquierda,HIGH);
          digitalWrite(SW_derecha,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'g'){ //SW_LEDINF
          digitalWrite(SW_ledInf,LOW);
          Serial.println(rd);
          }
          else if (rd == 'h'){
          digitalWrite(SW_ledInf,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'i'){ //SW_LEDSUP
          digitalWrite(SW_ledSup,LOW);
          Serial.println(rd);
          }
          else if (rd == 'j'){
          digitalWrite(SW_ledSup,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'k'){ //SW_luzAlta
          digitalWrite(SW_luzAlta,LOW);
          Serial.println(rd);
          }
          else if (rd == 'l'){
          digitalWrite(SW_luzAlta,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'm'){ //SW_CLAXON
          digitalWrite(SW_claxon,LOW);
          Serial.println(rd);
          delay(500);
          }
          else if (rd == 'n'){
          digitalWrite(SW_claxon,HIGH);
          Serial.println(rd);
          delay(500);
          }
          else if (rd == 'o'){ //SW_velocidad1
          digitalWrite(SW_velocidad1,LOW);
          Serial.println(rd);
          }
          else if (rd == 'p'){
          digitalWrite(SW_velocidad1,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'q'){ //SW_velocidad2
          digitalWrite(SW_velocidad2,LOW);
          Serial.println(rd);
          }
          else if (rd == 'r'){
          digitalWrite(SW_velocidad2,HIGH);
          Serial.println(rd);
          }
          else if (rd == 's'){ //SW_intermitente
          digitalWrite(SW_derecha,LOW);
          digitalWrite(SW_izquierda,LOW);
          Serial.println(rd);
          }
          else if (rd == 't'){
          digitalWrite(SW_derecha,HIGH);
          digitalWrite(SW_izquierda,HIGH);
          Serial.println(rd);
          }
          else if (rd == 'u')
          {
          digitalWrite(Bit1, LOW); //000
          digitalWrite(Bit2, LOW);
          digitalWrite(Bit3, LOW);
          }
          else if (rd == 'v')
          {
          digitalWrite(Bit1, LOW); //001
          digitalWrite(Bit2, LOW);
          digitalWrite(Bit3, HIGH);
          }
          else if (rd == 'w')
          {
          digitalWrite(Bit1, LOW); //010
          digitalWrite(Bit2, HIGH);
          digitalWrite(Bit3, LOW);
          }
          else if (rd == 'x')
          {
          digitalWrite(Bit1, HIGH); //011
          digitalWrite(Bit2, HIGH);
          digitalWrite(Bit3, LOW);
          }
          else if (rd == 'y')
          {
          digitalWrite(Bit1, LOW); //100
          digitalWrite(Bit2, LOW);
          digitalWrite(Bit3, HIGH);
          }
          else if (rd == 'z')
          {
          digitalWrite(Bit1, HIGH); //101
          digitalWrite(Bit2, LOW);
          digitalWrite(Bit3, HIGH);
          }
          else if (rd == 'ñ')
          {
          digitalWrite(Bit1, HIGH); //111
          digitalWrite(Bit2, HIGH);
          digitalWrite(Bit3, HIGH);
          }
      }
    //else if (rd1 == 'b') 
  }
  }
 }
} 
