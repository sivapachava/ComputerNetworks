import json
import rsa

class encryption:
    def __init__(self,sprivateKey,respublicKey,data,name):
        self.sprivateKey = sprivateKey
        self.respublicKey = respublicKey
        self.data = data
        self.name = name

    ## for authentication of the sender
    def digitalSignature(self):
        message = json.dumps(self.data)
        encodedMessage = message.encode('utf8')
        digitalSign = rsa.encrypt(encodedMessage,self.sprivateKey)
        digitalSign1 =  str(digitalSign)
        return digitalSign1

   ## maintain confidentiality for sender and receiver
    def encryptedMessage(self):
        encodedMessage = str(self.name).encode('utf8')
        encriptedMessage = rsa.encrypt(encodedMessage,self.respublicKey)
        print(type(encriptedMessage))
        encriptedMessage1 = str(encriptedMessage)
        return encriptedMessage1







