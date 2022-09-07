# This is always a post request type and also it is the part of tracker
# sender side
import json
class RequestCreation:
    def __init__(self,message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "P" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "U" + str[1:]
        return mType


    def final(self):
        final = self.requestType() + self.messageType() + str(self.message)
        return final
