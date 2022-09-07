# This is always a get request type
# request side
class HistoryRequestCreation:
    def __init__(self,message):
        self.message=message


    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "H" + str[1:]
        return mType

    def data(self):
        data = self.message
        return str(data)

    def final(self):
        final = self.requestType() + self.messageType() + self.data()
        finalMessage = final.encode('utf-8')
        return finalMessage

#response

class HistoryResponse:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "X" + str[1:]
        return mType


    def final(self):
        final = self.requestType() + self.messageType() + str(self.message)
        return final


# request side
class HistoryDataExtraction:
    def __init__(self,message):
        self.message = message

    def finalDataExtraction(self):
        pass


