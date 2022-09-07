# This is always a post request type
# sender side
import json
class BlockRequestCreation:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "P" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "N" + str[1:]
        return mType

    def data(self):
        str = "[]"
        data = json.dumps(self.message)
        dType = str[:1] + data + str[1:]
        return dType

    def final(self):
        final = self.requestType() + self.messageType() + self.data()
        finalMessage = final.encode('utf-8')
        print("finalMessageslksdjfndjdjfjdfjsdfn",finalMessage)
        return finalMessage

# receiver side
class BlockDataExtraction:
    def __init__(self,receivedMessage):
        self.receivedMessage = receivedMessage

    def finalDataExtraction(self):
        decodedMessage  = self.receivedMessage
        print("decodeMessage", decodedMessage)
        data = decodedMessage[7:-1]
        print("test",data)
        dict = json.loads(data)
        try:
         extractedData =(dict["hash"],dict["Block"]["Header"]["Version"],dict["Block"]["Header"]["PreviousHash"],str(dict["Block"]["Header"]["MerkleRoot"]),dict["Block"]["Header"]["Timestamp"],dict["Block"]["Header"]["DifficultyTarget"],dict["Block"]["Header"]["Nonce"],dict["Block"]["TransactionCounter"],str(dict["Block"]["TransactionList"]["Transactions"]))
        except:
         extractedData = (dict["hash"], dict["Block"]["Header"]["Version"], dict["Block"]["Header"]["PreviousHash"],
                             str(dict["Block"]["Header"]["MerkleRoot"]), dict["Block"]["Header"]["Timestamp"],
                             dict["Block"]["Header"]["DifficultyTarget"], dict["Block"]["Header"]["Nonce"],
                             dict["Block"]["TransactionCounter"], str(dict["Block"]["TransactionList"]))
        return extractedData

    def genesisBlockExtraction(self,message):
        dict = message
        data = (dict["hash"], dict["Block"]["Header"]["Version"], dict["Block"]["Header"]["PreviousHash"],
                             str(dict["Block"]["Header"]["MerkleRoot"]), dict["Block"]["Header"]["Timestamp"],
                              dict["Block"]["Header"]["DifficultyTarget"], dict["Block"]["Header"]["Nonce"],
                             dict["Block"]["TransactionCounter"], str(dict["Block"]["TransactionList"]))
        return  data



