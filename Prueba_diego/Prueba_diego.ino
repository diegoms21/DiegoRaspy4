const int Bit1 = 4;//menos sigmificativo
const int Bit2 = 3;
const int Bit3 = 2;//mas significativo

void setup(){
pinMode(Bit1,OUTPUT);
pinMode(Bit2,OUTPUT);
pinMode(Bit3,OUTPUT);
Serial.begin(9600);

}

void loop(){

  //000
  
  digitalWrite(Bit1,LOW);
  digitalWrite(Bit2,LOW);
  digitalWrite(Bit3,LOW);
  Serial.println("000");
  delay(5000);
  //001
  digitalWrite(Bit1,HIGH);
  digitalWrite(Bit2,LOW);
  digitalWrite(Bit3,LOW);
  Serial.println("001");
  delay(5000);
  //010
  digitalWrite(Bit1,LOW);
  digitalWrite(Bit2,HIGH);
  digitalWrite(Bit3,LOW);
  Serial.println("010");
  delay(5000);
  //011
  digitalWrite(Bit1,HIGH);
  digitalWrite(Bit2,HIGH);
  digitalWrite(Bit3,LOW);
  Serial.println("011");
  delay(5000);
  //100
  digitalWrite(Bit1,LOW);
  digitalWrite(Bit2,LOW);
  digitalWrite(Bit3,HIGH);
  Serial.println("100");
  delay(5000);
  //101
  digitalWrite(Bit1,HIGH);
  digitalWrite(Bit2,LOW);
  digitalWrite(Bit3,HIGH);
  Serial.println("101");
  delay(5000);
  //110
  digitalWrite(Bit1,LOW);
  digitalWrite(Bit2,HIGH);
  digitalWrite(Bit3,HIGH);
  Serial.println("110");
  delay(5000);
  //111
  digitalWrite(Bit1,HIGH);
  digitalWrite(Bit2,HIGH);
  digitalWrite(Bit3,HIGH);
  Serial.println("111");
  delay(5000);
  

  
}

