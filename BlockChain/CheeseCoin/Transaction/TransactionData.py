class TransactionData:
    def __init__(self, amount, message):
        self.amount = amount
        self.message = message

    def createMessage(self):
        data = {
        }
        data["Amount"] = self.amount
        data["message"] = self.message
        return data
