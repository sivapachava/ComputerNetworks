import json
import hashlib


class Mining:
    def __init__(self, createdBlock):
        self.createdBlock = createdBlock

    def createHash(self):
        block = json.dumps(self.createdBlock)
        hashBlock = hashlib.sha256(block.encode()).hexdigest()
        return hashBlock

    def mining(self):
        mineComplete = 0
        fullBlock = {
        }
        for i in range(0, 1000000):
            self.createdBlock['Header']['Nonce'] = i
            print("noncesjas", self.createdBlock['Header']['Nonce'])
            hashBlock = hashlib.sha256(str(self.createdBlock).encode()).hexdigest()
            print(hashBlock)
            if hashBlock[0] == '0' and hashBlock[1] == '0' and hashBlock[2] == '0' and hashBlock[3] == '0':
                mineComplete  =  1
                break

        fullBlock["index"] = ""
        fullBlock["hash"] = hashBlock
        fullBlock["Block"] = self.createdBlock
        return fullBlock,mineComplete