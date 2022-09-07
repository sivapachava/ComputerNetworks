import hashlib
import datetime


class Transactions:
    def __init__(self, senderName, recieverName, message):
        self.senderName = senderName
        self.recieverName = recieverName
        self.message = message

    def createTransaction(self):
        transaction = {
        }
        transactionIDCreation = str(self.senderName) + str(self.recieverName) + str(self.message)
        transaction["TransactionID"] = hashlib.sha1(transactionIDCreation.encode()).hexdigest()
        transaction["Sendername"] = self.senderName
        transaction["Receivername"] = self.recieverName
        transaction["Dateandtime"] = str(datetime.datetime.now())
        transaction["Data"] = self.message
        return transaction

