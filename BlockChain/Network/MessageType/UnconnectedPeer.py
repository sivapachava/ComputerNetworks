class UnconnectedDataExtraction:
    def __init__(self,receivedMessage):
        self.receivedMessage = receivedMessage

    def finalDataExtraction(self):
        decodedMessage  = self.receivedMessage
        data = eval(decodedMessage[7:-1])

        return data
