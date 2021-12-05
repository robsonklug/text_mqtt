# Para o uso da biblioteca MQTT é necessário instalar com o seguinte comando:
# pip3 install paho-mqtt

import paho.mqtt.client as mqtt

#Usando o servidor test.mosquito.org
#A classe (da biblioteca PAHO) fornece todas as funções necessárias para se conectar a 
# um broker MQTT, publicar mensagens, assinar tópicos e receber mensagens.
x_broker = "test.mosquitto.org"
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

    client.subscribe(x_topic, qos=0)

def on_message(client, userdata, msg):
    print("sisub: msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))

# criando o objeto client. Esta classe usa 4 parametros opcionais
obj_client = mqtt.Client(client_id=x_clientID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

obj_client.on_connect = on_connect
obj_client.on_message = on_message

obj_client.username_pw_set(None, password=None)
obj_client.connect(x_broker, port=1883, keepalive=60)

obj_client.loop_forever()

## Para funcionar o Publush e o Subscribe, é necessário abrir duas instancias rodando ao mesmo tempo. 
## Ao passo que a informações (neste caso o número aleatório) são atualizadas, o Subscribe recebe esta informação