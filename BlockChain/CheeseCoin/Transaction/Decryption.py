import json
import rsa


class decryption:
    def __init__(self, resprivateKey, senderpublicKey, encryptedData):
        self.resprivateKey = resprivateKey
        self.senderpublicKey = senderpublicKey
        self.encryptedData = encryptedData

    ## decryption procedure of data in the reciever
    def decryptMessage1(self):
        data = rsa.decrypt(self.encryptedData, self.resprivateKey)
        data2 = rsa.decrypt(data, self.senderpublicKey)
        decodeddata = data2.decode('utf8')
        final = json.loads(decodeddata)
        return final

