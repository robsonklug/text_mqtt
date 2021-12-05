import random
import time

import paho.mqtt.client as mqtt

#Usando o servidor test.mosquito.org
#A classe (da biblioteca PAHO) fornece todas as funções necessárias para se conectar a 
# um broker MQTT, publicar mensagens, assinar tópicos e receber mensagens.
x_broquer = "test.mosquitto.org"
x_topic = "$KLUG"
x_clientID = ""
 
## realizando a conexão e recebendo o retorno do status da conexão rc.
## rc (código de retorno), é usado para verificar se a conexão foi estabelecida que são:
## 0: Conexão bem-sucedida
## 1: Conexão recusada - versão de protocolo incorreta
## 2: Conexão recusada - identificador de cliente inválido
## 3: Conexão recusada - servidor indisponível
## 4: Conexão recusada - nome de usuário ou senha incorretos
## 5: Conexão recusada - não autorizada
def on_connect(client, userdata, flags, rc):
    if (rc == 0):
        print("Conexão OK. Retorno: ", client._host, " Porta: ", client._port)
    else:
        print("Conexão Falha. Retorno:  ", client._host, "port: ", client._port,"Flags: ", flags )
      

def on_publish(client, userdata, mid):
    print("sipub: msg published (mid={})".format(mid))

client = mqtt.Client(client_id=x_clientID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(None, password=None)
client.connect(x_broquer, port=1883, keepalive=60)

client.loop_start()

while True:

    msg_to_be_sent = random.randint(0, 100) 
    client.publish(x_topic, 
                   payload=msg_to_be_sent, 
                   qos=0, 
                   retain=False)
    print("Envio:", msg_to_be_sent)

    time.sleep(10)

client.loop_stop()