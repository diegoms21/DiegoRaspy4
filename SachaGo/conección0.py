import paho.mqtt.client as mqtt
cliente = mqtt.Client()

cliente.connect("musach.tk",1883)
val = "cholito,lokochef1,0poseidon"
cliente.publish("values",val)
#print("cholito")