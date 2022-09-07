from threading import Thread
from Tracker.server.server import Tracker
from Tracker.Queue.QueueThreading import Queue
from pathlib import Path
from Tracker.Database.Creation import CreateDatabase
from Tracker.Database.PeerDetails import PeerDetailsTable
from Tracker.Database.RegisteredPeers import RegisteredPeerTable
from Tracker.MessageFormat.SendUnconnected import RequestCreation
from Tracker.MessageFormat.RequestConnected import ConnectedRequest
import time
import socket
#########################################################################################################
# tracker connection details
ip = socket.gethostbyname(socket.gethostname())
port = 7070
connection = (ip, port)
##########################################################################################################
if Path('./Tracker/DatabaseSource/Tracker.db').is_file():
    print("DataBaseAlreadyCreated")
else:
    dataBaseCreation = CreateDatabase()

peerDataTable = PeerDetailsTable()
peerDataTable.createTable()
tracker = Tracker(connection)
#Created Registered peers table
createdRegisteredPeers = RegisteredPeerTable()
createdRegisteredPeers.createRegisteredTable()
############################################################################################################
#Automatic liviliness test for the peers
def livelinesstest():
    while True:
       print("Doing Liveliness Test")
       time.sleep(60)
       connectionDetails = createdRegisteredPeers.retrieveRegisteredElements()
       print("Connected peers list:",connectionDetails)
       unconnectedPeers = tracker.liveness(connectionDetails,"00000")
       print("unconnected peers list:", unconnectedPeers )
       if (len(unconnectedPeers) != 0):
           requestMessage  = RequestCreation(unconnectedPeers)
           messageFormatUnconnected = requestMessage.final()
           print("Message Format Unconnected",messageFormatUnconnected)
           connectionDetails = peerDataTable.retrieveElements()
           print(connectionDetails)
           print("SendingMessage")
           print(requestMessage.final())
           tracker.sendNewNode(connectionDetails,messageFormatUnconnected)
       print("succeed")

#liviliness test
livelinessTest = Thread(target=livelinesstest)
livelinessTest.start()



if __name__ == "__main__":
    while True:
        trackerReceiverQueue = Queue()
        receiveData = Thread(target=tracker.receiveNewNode, args=(trackerReceiverQueue,))
        receiveData.start()
        receiveData.join()
        receivedMessage = trackerReceiverQueue.dequeue()
        print(type(receivedMessage))
        print(receivedMessage)
        if receivedMessage[4] == "J":
            extractReceivedData = tracker.extractIP()
            print(extractReceivedData)
            peerDataTable.addElements(extractReceivedData)
            createdRegisteredPeers.addRegisteredElements(extractReceivedData)
            connectionDetails = peerDataTable.retrieveElements()
            tracker.sendNewNode(connectionDetails, receivedMessage)

        #send the connected peers
        if receivedMessage[4] == "R":
           connectedPeerList =  peerDataTable.retrieveAllSelected()
           print(connectedPeerList)
           connectedMessageRequest = ConnectedRequest(connectedPeerList)
           print(connectedMessageRequest.final())






