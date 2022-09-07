# This is always a post request type
# sender side
import json
class RequestCreation:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "T" + str[1:]
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
    def __init__(self,receivedMessage):
        self.receivedMessage = receivedMessage

    def finalDataExtraction(self):
        decodedMessage  = self.receivedMessage
        data = decodedMessage[7:-1]
        dataDict  = json.loads(data)
        print("data:::",dataDict)
        finalTuple = (dataDict["Dateandtime"],dataDict["TransactionID"],dataDict["Sendername"],dataDict["Data"]["Message"],dataDict["Data"]["DigitalSignature"])
        print("final tuple",finalTuple)
        ledgerTuple = (dataDict["Dateandtime"],dataDict["TransactionID"],dataDict["Sendername"],dataDict["Receivername"],dataDict["Data"]["Message"],dataDict["Data"]["DigitalSignature"])
        print(ledgerTuple)
        return finalTuple



