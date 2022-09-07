class TransactionsLedger:
    def __init__(self, transactions):
        self.transactions = transactions
        self.Ledgerlist = []

    def createtransactionlist(self):
        for transaction in self.transactions:
            dict = {

            }
            dict["index"] = self.transactions.index(transaction) + 1
            dict["DataAndTime"] = transaction[0]
            dict["TransactionID"] = transaction[1]
            dict["SenderName"] = transaction[2]
            dict["ReceiverName"] = transaction[3]
            dict["Data(Amount and Message)"] = transaction[4]
            dict["DigitalSignature"] = transaction[5]
            self.Ledgerlist.append(dict)
        return self.Ledgerlist
