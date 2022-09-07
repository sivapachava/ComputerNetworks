class ConnectedRequest:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "R" + str[1:]
        return mType


    def final(self):
        final = self.requestType() + self.messageType() + str(self.message)
        return final
