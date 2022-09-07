# This is always a post request type
# sender side
import json
class PeerNewData:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "P" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "J" + str[1:]
        return mType

    def data(self):
        str = "[]"
        data = json.dumps(self.message)
        dType = str[:1] + data + str[1:]
        return dType

    def final(self):
        final = self.requestType() + self.messageType() + self.data()
        finalMessage = final.encode('utf-8')
        return finalMessage

# receiver side
class DataExtraction:
    def __init__(self,receivedMessage,peerList):
        self.receivedMessage = receivedMessage
        self.peerList = peerList

    def finalDataExtraction(self):
        data = self.receivedMessage[7:-1]
        final = json.loads(data)
        port = final['port']
        ipaddress = final['ipaddress']
        name = final['name']
        publickey = final['publickey']
        finalTuple = (name, publickey,ipaddress,int(port))
        return finalTuple



