import hashlib
import datetime
import json


class genesisBlock:
    def __init__(self, name):
        self.name = name

    def transaction(self):
        transactionDict = {
        }
        transactionDict["name"] = self.name
        transactionDict["TransactionID"] = hashlib.sha1(str(self.name).encode()).hexdigest()
        transactionDict["Timestamp"] = str(datetime.datetime.now())
        transactionDict["TransactionType"] = "Reward Transaction"
        return transactionDict

    def createHeader(self):
        header = {
        }
        header["Version"] = "v1"
        header["PreviousHash"] = "000000000000000000000000000000000000000000000"
        hashRewardTransaction = json.dumps(self.transaction())
        header["MerkleRoot"] = hashlib.sha1(str(hashRewardTransaction).encode()).hexdigest()
        header["Timestamp"] = str(datetime.datetime.now())
        header["DifficultyTarget"] = "4"
        return header

    def genesisBlockCreation(self):
        block = {
        }
        block["Size"] = ""
        block["Header"] = self.createHeader()
        block["TransactionCounter"] = "1"
        block["TransactionList"] = self.transaction()
        return block

    def createHash(self):
        block = str(self.genesisBlockCreation())
        hashBlock = hashlib.sha256(block.encode()).hexdigest()
        return hashBlock

    def mining(self):
        createdBlock = self.genesisBlockCreation()
        GenesisBlock = {
        }
        for i in range(0, 10000000):
            createdBlock['Header']['Nonce'] = i
            print("noncesjas", createdBlock['Header']['Nonce'])
            hashBlock = hashlib.sha256(str(createdBlock).encode()).hexdigest()
            print(hashBlock)
            if hashBlock[0] == '0' and hashBlock[1] == '0' and hashBlock[2] == '0' and hashBlock[3] == '0':
                break

        GenesisBlock["index"] = "0"
        GenesisBlock["hash"] = hashBlock
        GenesisBlock["Block"] = createdBlock
        return GenesisBlock





