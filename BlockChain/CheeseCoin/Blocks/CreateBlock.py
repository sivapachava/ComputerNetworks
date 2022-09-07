import datetime
import hashlib


class Block:
    def __init__(self, version, previousHash, merkleRoot, difficultyTarget, nonce, transactionList, name):
        self.version = version
        self.previousHash = previousHash
        self.merkleRoot = merkleRoot
        self.difficultyTarget = difficultyTarget
        self.nonce = nonce
        self.transactionList = transactionList
        self.name = name

    def createHeader(self):
        header = {

        }
        header["Version"] = self.version
        header["PreviousHash"] = self.previousHash
        header["MerkleRoot"] = self.merkleRoot
        header["Timestamp"] = str(datetime.datetime.now())
        header["DifficultyTarget"] = self.difficultyTarget
        header["Nonce"] = self.nonce
        return header

    def rewardTransaction(self):
        rewardTransaction = {}
        rewardTransaction["name"] = self.name
        rewardTransaction["TransactionID"] = hashlib.sha1(str(self.name).encode()).hexdigest()
        rewardTransaction["Timestamp"] = str(datetime.datetime.now())
        rewardTransaction["TransactionType"] = "Reward Transaction"
        return rewardTransaction

    def createTransactionList(self):
        transactions = {

        }

        transactions["Transactions"] = self.transactionList
        transactions["Transactions"] = self.rewardTransaction()


        return transactions

    def transactionCounter(self):
        return len(self.transactionList)

    def createBlocks(self):
        block = {
        }
        block["Header"] = self.createHeader()
        block["TransactionCounter"] = self.transactionCounter()
        block["TransactionList"] = self.createTransactionList()
        return block
