# This is always a post request type
# sender side
import json
class LedgerRequestCreation:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "P" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "L" + str[1:]
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
class LedgerDataExtraction:
    def __init__(self,receivedMessage):
        self.receivedMessage = receivedMessage

    def finalDataExtraction(self):
        decodedMessage  = self.receivedMessage
        data = decodedMessage[7:-1]
        dataDict = json.loads(data)
        ledgerTuple = (
        dataDict["Dateandtime"], dataDict["TransactionID"], dataDict["Sendername"], dataDict["Receivername"],
        dataDict["Data"]["Message"], dataDict["Data"]["DigitalSignature"])
        print(ledgerTuple)
        return ledgerTuple



