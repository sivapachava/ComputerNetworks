
class PeerDetails:
    def __init__(self, ipAddress, port,publicKey,name):
        self.ipAddress = ipAddress
        self.port = port
        self.publicKey = publicKey
        self.name = name

    def createMessage(self):
        message = {
        }
        message["name"] = self.name
        message["port"] = self.port
        message["ipaddress"] = self.ipAddress
        message["publickey"] = str(self.publicKey)
        return message

