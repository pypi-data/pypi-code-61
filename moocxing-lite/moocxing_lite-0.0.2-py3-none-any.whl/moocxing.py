from .MXMedia import MXMedia
from .MXSpeech import MXSpeech
from .MXNLP import MXNLP
from .MXSerial import MXSerial
from .MXMqtt import MXMqtt


class MOOCXING():
    def __init__(self):
        pass

    '''初始化'''

    def initMedia(self):
        return MXMedia()

    def initSpeech(self, APP_ID, API_KEY, SECRET_KEY):
        return MXSpeech(APP_ID, API_KEY, SECRET_KEY)

    def initNLP(self, APP_ID, API_KEY, SECRET_KEY):
        return MXNLP(APP_ID, API_KEY, SECRET_KEY)

    def initMinecraft(self, address="localhost", port=4711):
        return Minecraft.create(address, port)

    def initMqtt(self, MQTTHOST="mqtt.16302.com", MQTTPORT=1883):
        return MXMqtt(MQTTHOST, MQTTPORT)

    def initSerial(self, com, bps):
        return MXSerial(com, bps)
        

    def getCom(self, num=-1):
        return MXSerial.getCom(num)
