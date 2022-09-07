# sender side
import json
class RequestConnected:
    def __init__(self):
       pass

    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "R" + str[1:]
        return mType

    def data(self):
        str = "[]"
        data = "RequestConnectedPeers"
        dType = str[:1] + data + str[1:]
        return dType

    def final(self):
        final = self.requestType() + self.messageType() + self.data()
        finalMessage = final.encode('utf-8')
        return finalMessage

class RequestConnectedExtraction:
    def __init__(self,message):
       self.message = message

    def extraction(self):
       data = self.message[6:]
       return eval(data)
