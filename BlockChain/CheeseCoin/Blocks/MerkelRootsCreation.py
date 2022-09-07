import hashlib
import json


class merkelroots:
    def __init__(self, transactionList):
        self.transactionList = transactionList

    def createTransactionListHash(self):
        hashTransactionList = []
        for i in range(0, len(self.transactionList)):
            message = str(self.transactionList[i])
            messageHash = hashlib.sha1(message.encode()).hexdigest()
            hashTransactionList.append(messageHash)
        return hashTransactionList

    def createMerkeltree(self, hasedTransactionList):
        list = []
        if (len(hasedTransactionList) % 2 == 0):
            for j in range(0, len(hasedTransactionList), 2):
                data = str(hasedTransactionList[j]) + str(hasedTransactionList[j + 1])
                hashData = hashlib.sha1(data.encode()).hexdigest()
                list.append(hashData)

        if (len(hasedTransactionList) % 2 != 0):
            for j in range(0, len(hasedTransactionList) - 1, 2):
                data = str(hasedTransactionList[j]) + str(hasedTransactionList[j + 1])
                hashData = hashlib.sha1(data.encode()).hexdigest()
                list.append(hashData)

            mes = hasedTransactionList[len(hasedTransactionList) - 1] + hasedTransactionList[
                len(hasedTransactionList) - 1]
            hasfMes = hashlib.sha1(str(mes).encode()).hexdigest()
            list.append(hasfMes)

        return list

    def createMerkelRoot(self):
        merkelRoot = self.createTransactionListHash()
        for j in range(len(self.createTransactionListHash())):
            merkeltree = self.createMerkeltree(merkelRoot)
            merkelRoot = merkeltree
            if (len(merkelRoot) == 1):
                break

        return merkelRoot

