from BlockChain.Network.TrackerClient.client import TrackerClient
from BlockChain.Network.TrackerClient.MessageCreationToTracker import PeerDetails
from BlockChain.CheeseCoin.Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from BlockChain.Network.MessageType.Join import PeerNewData
from BlockChain.CheeseCoin.Transaction.TransactionData import TransactionData
from BlockChain.CheeseCoin.Transaction.Encryption import encryption
from BlockChain.CheeseCoin.Transaction.CreateTransactionData import Transactions
from BlockChain.Network.MessageType.Transaction import RequestCreation as TransactionRequestCreation
from BlockChain.Network.RequestType.BroadcastSelected import BroadCastSelected
from BlockChain.Network.MessageType.TransactionLedger import LedgerRequestCreation
from BlockChain.Network.RequestType.BroadcastMultiple import BroadCastMulitple
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Ledger import TransactionsLedgerDT
from BlockChain.CheeseCoin.Transaction.CreateTransactionDictionaryLedger import TransactionsLedger
from BlockChain.CheeseCoin.Blocks.MerkelRootsCreation import merkelroots
from BlockChain.CheeseCoin.Blocks.CreateBlock import Block
from BlockChain.CheeseCoin.Blocks.BlockMining import Mining
from BlockChain.Network.MessageType.MineComplete import RequestCreation
from BlockChain.Database.MineComplete import MiningCompleteStatusDT
from BlockChain.Network.MessageType.NewBlock import BlockRequestCreation
from BlockChain.Database.BlockChain import BlockChainDT
from BlockChain.Database.CurrentPeerData import PeerData
from BlockChain.Network.MessageType.RequestConnected import RequestConnected
from BlockChain.Network.MessageType.History import HistoryRequestCreation

import time
import socket

################################################################################################################
#database for the connected peer details
connectedPeers  = PeerDetailsTable()
#database for the ledger
ledgerDataTable  = TransactionsLedgerDT()
#database for the getting miningstatus
miningCompleteStatusTable = MiningCompleteStatusDT()
#database for the blockchain
blockchainTable  =  BlockChainDT()
#create table for storing the self peer data
createPeer = PeerData()

################################################################################################################
if __name__ == "__main__":
    ############################################################################################################
    # Private key and Public key generation
    hostGeneratePublicPrivateKey = generatePublicPrivateKey
    hostPublicPrivateKey = hostGeneratePublicPrivateKey.generatePubPriKeyPair()
    hostPublicKey = hostPublicPrivateKey[0]
    hostPrivateKey = hostPublicPrivateKey[1]
    print("type of private key", type(hostPrivateKey))
    print("type of public key", type(hostPublicKey))
    ############################################################################################################
    # create tracker client object and message creation to send the connection details to the tracker
    # Tracker network details
    trackerIP = "192.168.43.202"
    trackerPort = 7070
    trackerTriple = (trackerIP,trackerPort)
    try:
      peerData = createPeer.retrivePeerData()
      print(peerData[0])
    except:
        # new peer details
        ipAddress = socket.gethostbyname(socket.gethostname())
        port = input("Enter the port to run the peer:")
        name = input("Enter your Name:")
        # storing this data to the user
        createPeer.addPeerData((name,int(port),ipAddress))
        # peer data converted to dictionary for sending
    #message creation(convert the below data to a dictionary)
    currentPeerDetails = createPeer.retrivePeerData()
    print("Peer Details :",currentPeerDetails)
    print("type of peer details",type(currentPeerDetails[0][1]))
    peerDetails = PeerDetails(currentPeerDetails[0][3], currentPeerDetails[0][2], hostPublicKey, currentPeerDetails[0][1])
    print("PeerName:",currentPeerDetails[0][1])
    print("Peer ID Address: ", currentPeerDetails[0][3])
    print("Peer Running at: ", currentPeerDetails[0][2])
    ###############################################################################################################################################


    while True:
        # select the operation need to do by the system
        print("################################################################################################################################################")
        print("Enter C or c to connect to the peer at the first time(means connect to the tracker)\nEnter R or r to request the connected peers form Tracker\nEnter T or t to send messrage and make transaction to the peers\nEnter M or m for mining the current transaction and create Block\nEnter B or b for request the complete blockchain")
        operation = input("Select the operation need to do:")

#####################################################################################################################################################
        #Select C or c to connect the new peer to the newtwork
        if operation == "C" or operation == "c":
            peerJsonData = peerDetails.createMessage()
            print("Dictionary Converted Peer Data : ",peerJsonData)
            # message creator while send the peer data to tracker
            peerMessageStructure = PeerNewData(peerJsonData)
            finalMessageStructure = peerMessageStructure.final()
            print("final message format of the new peer details to the tracker:",finalMessageStructure)
            #send the final message to the tracker
            trackerClient = TrackerClient(trackerTriple,finalMessageStructure)
            trackerClient.trackerClient()

#############################################################################################################################################
        #Select t or T to do individual transactions
        if operation == "T" or operation == "t":
            print("Connected Peers Name",connectedPeers.retreievePeerName())
            receiverName = input("Select the receiver name from the list:")
            amount = input("Enter the transaction amount:")
            message = input("Enter the message to send :")
            receiverPeerDetails = connectedPeers.retrieveAllSelected(receiverName)
            print("selected peer details:", receiverPeerDetails)
            #####################################################################################################
            #convert the transmitted message to a json string
            transactionMessage = TransactionData(amount, message)
            data = transactionMessage.createMessage()
            print("message and amount to be send", data)
            ######################################################################################################
            # Encryption of the message
            oencryption = encryption(hostPrivateKey,hostPublicKey, data, currentPeerDetails[0][1])
            digtalSignature = oencryption.digitalSignature()
            print("vcfg", digtalSignature)
            encryptedData = oencryption.encryptedMessage()
            print(encryptedData)
            print("type of " , type(encryptedData))
            finalMessage = {"Message": encryptedData, "DigitalSignature": digtalSignature}
            print("EncryptedData", finalMessage)
            ####################################################################################################
            # Creating the transaction details
            transactureStructure = Transactions(currentPeerDetails[0][1], receiverName, finalMessage)
            transactionFullMessage = transactureStructure.createTransaction()
            print("TransactionMessage", transactionFullMessage)
            ######################################################################################################
            transaction = TransactionRequestCreation(transactionFullMessage)
            finalEncodeMessage = transaction.final()
            print("Final Encoded Message for sending :",finalEncodeMessage)
            ######################################################################################################
            #send the message to the selected peer
            sendMessage  = BroadCastSelected((receiverPeerDetails[2],receiverPeerDetails[3]),finalEncodeMessage)
            sendMessage.sPeer()
            time.sleep(2)
            #######################################################################################################
            ledgerRequestCreation = LedgerRequestCreation(transactionFullMessage)
            ledgerMessage = ledgerRequestCreation.final()
            print("Converted Transaction Message to send to other peers format:", ledgerMessage)
            connectedPeersList = connectedPeers .retrieveElements()
            broadCastTransactions = BroadCastMulitple (connectedPeersList, ledgerMessage)
            broadCastTransactions.mPeer()

        if operation == "M" or operation == "m":
            transactionLedgerList  = ledgerDataTable.retriveLedgerElement()
            print("TransactionLedger" , transactionLedgerList)
            ledger = TransactionsLedger(transactionLedgerList)
            ledgerData = ledger.createtransactionlist()
            print(ledgerData)
            merkalRootCreation = merkelroots(ledgerData)
            createdMerkalRoot = merkalRootCreation.createMerkelRoot()
            print(createdMerkalRoot )
            #Block Creation
            version = "V1"
            previousHash = blockchainTable.retriveLastHash()[0]
            merkleRoot = createdMerkalRoot
            difficultyTarget = "4"
            nonce = 0
            blockCreation = Block(version,previousHash,merkleRoot,difficultyTarget,nonce,ledgerData,currentPeerDetails[0][1])
            createdBloc = blockCreation.createBlocks()
            print(createdBloc)
            #mining logic
            mineCreatedBlock = Mining(createdBloc)
            minedBlock = mineCreatedBlock.mining()
            print("Final Created Block", minedBlock[0])
            miningPeerStatus =  miningCompleteStatusTable.retriveMiningStatus()
            ########################################################################################################
            #Proof of Work
            try:
               print("miningPeerStatus",miningPeerStatus[0])
               print("Block is already mined")
            except:
               addBlock = 1
            ##########################################################################################################
               mineCompleteRequestCreation = RequestCreation("MineCompleted")
               mineCompleteMessage = mineCompleteRequestCreation.final()
               print("Mine Complete Message Format :", mineCompleteMessage)
               connectedPeersList1 = connectedPeers.retrieveElements()
               broadCastMineCompleteMessage = BroadCastMulitple(connectedPeersList1, mineCompleteMessage)
               broadCastMineCompleteMessage.mPeer()
               blockRequestCreation = BlockRequestCreation(minedBlock[0])
               print("final request creation", blockRequestCreation.final())
               broadCastBlock = BroadCastMulitple(connectedPeersList1, blockRequestCreation.final())
               broadCastBlock.mPeer()
               addBlock = 0

            miningCompleteStatusTable.deleteMiningStatus()
            ledgerDataTable.deleteLedgerElement()

       #for sending the blockchain copy to newly joined peers
        if operation == "B" or operation == "b":
            print("Connected Peers Name", connectedPeers.retreievePeerName())
            blockName = input("Select the peer name:")
            selectedPeer = connectedPeers.retrieveAllSelected(blockName)
            print(selectedPeer[2],selectedPeer[3])
            history = HistoryRequestCreation((selectedPeer[2],selectedPeer[3]))
            print(history.final())
            requestHistory = BroadCastSelected((selectedPeer[2],selectedPeer[3]),history.final())
            requestHistory.sPeer()



        #requesting all connected network details
        if operation == "R" or operation == "r":
            requestConnectedMessageCreation = RequestConnected()
            requestConnectedMessageCreation.final()
            print(requestConnectedMessageCreation.final())
            # send the final message to the tracker
            trackerClient = TrackerClient(trackerTriple, requestConnectedMessageCreation.final())
            trackerClient.trackerClient()

