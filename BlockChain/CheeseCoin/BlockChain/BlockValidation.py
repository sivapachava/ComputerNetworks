from BlockChain.Database.BlockChain import BlockChainDT
from BlockChain.Database.BlockChainValidationResults import BlockChainValidation
import time


class BlockValidation:
    def __init__(self):
        pass

    def blockValidation(self):
        blockChain = BlockChainDT()
        blockChainValidation = BlockChainValidation()
        while True:
            time.sleep(60)
            print("sequence number and corresponding hash", blockChain.retrieveBlockVaidation())
            blockDetails = blockChain.retrieveBlockVaidation()
            for block in blockDetails:
                if (block[1][0] == '0') and (block[1][1] == '0') and (block[1][2] == '0') and (
                        block[1][3] == '0' and block[0] == blockDetails.index(block) + 1):
                    print("block validation successfull", block[1][0], block[1][1], block[1][2], block[1][3])
                    blockChainValidation.addBlockChainValidation((block[0], "Block Validation Success"))
                else:
                    print("invalid Block", block[1][0], block[1][1], block[1][2], block[1][3])
                    blockChainValidation.addBlockChainValidation((block[0], "Block Validation Failed"))
