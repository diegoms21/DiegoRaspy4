//#include <Arduino.h>

const int izquierda = 13 ; //rele 1
const int derecha = 12; //rele 2
const int SW_ledSup = 11 ; //rele 3
const int SW_ledInf = 10; //rele 4
const int SW_LuzAlta = 9 ; //rele 5
const int SW_llave = 8; //rele 6

void setup() {
Serial.begin(9600);
pinMode(izquierda,OUTPUT);
pinMode(derecha,OUTPUT);
pinMode(SW_ledSup,OUTPUT);
pinMode(SW_ledInf,OUTPUT);
pinMode(SW_LuzAlta,OUTPUT);
pinMode(SW_llave,OUTPUT);

digitalWrite(izquierda,HIGH);
digitalWrite(derecha,HIGH);
digitalWrite(SW_ledSup,HIGH);
digitalWrite(SW_ledInf,HIGH);
digitalWrite(SW_LuzAlta,HIGH);
digitalWrite(SW_llave,HIGH);
}

void loop() {
  
  if (Serial.available() > 0){
  char rd = Serial.read();
  Serial.print(rd);
  
    //RELE 6 LLAVE
    if (rd == 'a'){
      digitalWrite(SW_llave,LOW);
      Serial.println(rd);
    }
    else if (rd == 'b'){
      digitalWrite(SW_llave,HIGH);
      Serial.println(rd);
     }
    //RELE 5 LUZ ALTA
    if (rd == 'c'){
      digitalWrite(SW_LuzAlta,LOW);
      Serial.println(rd);
    }
    else if (rd == 'd'){
      digitalWrite(SW_LuzAlta,HIGH);
      Serial.println(rd);
    }
      //RELE 4 LUZ LED INF
    if (rd == 'e'){
      digitalWrite(SW_ledInf,LOW);
      Serial.println(rd);
    }
    else if (rd == 'f'){
      digitalWrite(SW_ledInf,HIGH);
      Serial.println(rd);
    }
      //RELE 3 LUZ LED SUP
    if (rd == 'g'){
      digitalWrite(SW_ledSup,LOW);
      Serial.println(rd);
    }
    else if (rd == 'h'){
      digitalWrite(SW_ledSup,HIGH);
      Serial.println(rd);
    }
      //RELE 2 derecha
    if (rd == 'i'){
      digitalWrite(derecha,LOW);
      Serial.println(rd);
    }
    else if (rd == 'j'){
      digitalWrite(derecha,HIGH);
      Serial.println(rd);
    }
      //RELE 1 izquierda
    if (rd == 'k'){
      digitalWrite(izquierda,LOW);
      Serial.println(rd);
    }
    else if (rd == 'l'){
      digitalWrite(izquierda,HIGH);
      Serial.println(rd);
  }
 }
} 
