import time
import subprocess
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def customSubackCallback(mid, data):
    print("Received SUBACK packet id: " + str(mid))

def onMessageRecieved(message):
    print(str(message.payload).strip("\""))
    if str(message.payload).strip("\"") == "SINGLE":
        print("Single Click")
        subprocess.call("python getMotoCords.py", shell=True)
    elif str(message.payload).strip("\"") == "DOUBLE":
        print("Double Click")
        subprocess.call("python secure_mot.py", shell=True)

# Init AWSIoTMQTTClient
lient = AWSIoTMQTTClient("receive")
topic = "dogcatdog/pickle"

lient.configureEndpoint("a39jupqojj41el.iot.us-west-2.amazonaws.com", 8883)
lient.configureCredentials(root-CA Key, Private Key, Public Key)

# AWSIoTMQTTClient connection configuration
lient.configureAutoReconnectBackoffTime(1, 32, 20)
lient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
lient.configureDrainingFrequency(2)  # Draining: 2 Hz
lient.configureConnectDisconnectTimeout(10)  # 10 sec
lient.configureMQTTOperationTimeout(5)  # 5 sec
lient.onMessage = onMessageRecieved
# Connect and subscribe to AWS IoT
lient.connect()
# Note that we are not putting a message callback here. We are using the general message notification callback.
lient.subscribeAsync(topic, 1, ackCallback=customSubackCallback)

while True:
    time.sleep(1)
