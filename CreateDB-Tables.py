from BlockChain.Database.CreateDatabase import Database
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Transactions import TransactionsDT
from BlockChain.Database.Ledger import TransactionsLedgerDT
from pathlib import Path
from BlockChain.Database.MineComplete import MiningCompleteStatusDT
from BlockChain.Database.BlockChain import BlockChainDT
from BlockChain.Database.CurrentPeerData import PeerData
from BlockChain.Database.MessageQueue import MessageQueue
from BlockChain.Database.BlockChainValidationResults import BlockChainValidation
if Path('./Database/BlockChain.db').is_file():
    print ("DataBaseAlreadyCreated")

else:
    print("File not exist")
    dataBaseCreation = Database()
###################################################################################
#create peer tables
createPeerTable = PeerDetailsTable()
createPeerTable.createTable()
###################################################################################
#create transaction datatable
createTransactionTable  =  TransactionsDT()
createTransactionTable.createTable()

###################################################################################
#create transaction ledger table
createLedgerDT = TransactionsLedgerDT()
createLedgerDT.createLedgerTable()

###################################################################################
#create mining status table
miningCompleteDataTable = MiningCompleteStatusDT()
miningCompleteDataTable.createTable()

###################################################################################
#create blockchain table
createBlockChainTable =  BlockChainDT()
createBlockChainTable.createBlockChainTable()

####################################################################################
#create currentpeerdata
createPeerTable = PeerData()
createPeerTable.createPeerDataTable()

#####################################################################################
#create the message queue table
createTableMessageQueue = MessageQueue()
createTableMessageQueue.createMessageTable()

##########################################################################################
#createblockchainvalidationtable
createBlockChainValidation = BlockChainValidation()
createBlockChainValidation.createBlockChainValidation()
