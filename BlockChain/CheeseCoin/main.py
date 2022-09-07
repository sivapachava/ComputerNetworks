#########################################################################################
# Blockchain working without networking Purpose of this program  is to test the logic and
# make sure the blockchain part is working as per the requirement fine without networking

from Transaction.TransactionData import TransactionData
from Transaction.CreateTransactionData import Transactions
from Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from Transaction.Encryption import encryption
from Transaction.CreateTransactionLedger import TransactionsLedger
from Blocks.MerkelRootsCreation import merkelroots
from Blocks.CreateBlock import Block
from Blocks.BlockMining import Mining
from BlockChain.BlockChain import BlockChain
from BlockChain.GenesisBlock import genesisBlock

if __name__ == "__main__":
    #######################################################################################
    # Private key and Public key generation
    senderGenerate = generatePublicPrivateKey
    receiverGenerate = generatePublicPrivateKey
    senderPublicPrivateKey = senderGenerate.generatePubPriKeyPair()
    recieverPublicPrivateKey = receiverGenerate.generatePubPriKeyPair()
    senderPublicKey = senderPublicPrivateKey[0]
    senderPrivateKey = senderPublicPrivateKey[1]
    receiverPublicKey = recieverPublicPrivateKey[0]
    receiverPrivateKey = recieverPublicPrivateKey[1]
    #########################################################################
    # Add genesis block
    GeneratedBlockChain = []
    createBlockChain = BlockChain()
    ocreateGenesisBlock = genesisBlock("Arun")
    createdGenesisBlock = ocreateGenesisBlock.mining()
    B = createBlockChain.addBlock(createdGenesisBlock)
    print(B)
    while True:
        operation = input(
            "Enter the operation you need to do\n Enter t or T for doing transaction \n Enter m or M to do mining : ")
        if (operation == "T" or operation == 't'):
            ######################################################################
            # Enter the sender and reciver details
            senderName = input("Enter the Sender Name:")
            receiverName = input("Enter the receiver name:")
            amount = input("Enter the amount:")
            message = input("Enter the message:")
            transactionMessage = TransactionData(amount, message)
            data = transactionMessage.createMessage()
            print("message and amount to be send", data)
            ######################################################################
            # Encryption of the message
            oencryption = encryption(senderPrivateKey, receiverPublicKey, data, senderName)
            digtalSignature = oencryption.digitalSignature()
            print("vcfg", digtalSignature)
            encryptedData = oencryption.encryptedMessage()
            print(encryptedData)
            finalMessage = {
            }
            finalMessage["Message"] = encryptedData
            finalMessage["DigitalSignature"] = digtalSignature
            print("EncryptedData", finalMessage)
            #######################################################################
            # Creating the transaction details
            transactureStructure = Transactions(senderName, receiverName, finalMessage)
            transactionFullMessage = transactureStructure.createTransaction()
            print("TransactionMessage", transactionFullMessage)
            #######################################################################
            # Creating the transaction list
            otransactionLedgerCreation = TransactionsLedger(transactionFullMessage)
            transactionList = otransactionLedgerCreation.createtransactionlist()
            print("TransactionList", transactionList)
        ################################################################################
        # Processing of Mining
        if (operation == "M" or operation == "m"):
            transactionLedger = transactionList
            print(transactionLedger)
            #################################################################################
            # Merkel Root Calculation
            omerkelroot = merkelroots(transactionLedger)
            createdMerkelRoot = omerkelroot.createMerkelRoot()
            print("Created Merkel Root", createdMerkelRoot)
            ##################################################################################
            # Block Creation
            version = "V1"
            previousHash = ""
            merkleroot = createdMerkelRoot
            difficultyTarget = "4"
            nonce = 0
            transact = transactionLedger
            oblock = Block(version, previousHash, merkleroot, difficultyTarget, nonce, transact)
            createdBlock = oblock.createBlocks()
            print(createdBlock)
            ####################################################################################
            # Mining Logic
            omining = Mining(createdBlock)
            minedBlock = omining.mining()
            print("Final Created Block", minedBlock)
            #####################################################################################
            # Add block to the chain
            fullBlockChain  = createBlockChain.addBlock(minedBlock)
            print(fullBlockChain)


