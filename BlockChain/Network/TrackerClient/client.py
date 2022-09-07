#Tracker Client sender program
import socket
from BlockChain.Network.MessageType.RequestConnected import RequestConnectedExtraction
from BlockChain.Database.PeerDetails import PeerDetailsTable

class TrackerClient:
    # connectDetails is a tuple which contain ipaddress and port number
    def __init__(self, connectDetails,message):
        self.connectDetails = connectDetails
        self.message = message
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.client)
        print("Trying to connect to the tracker.................")
        try:
         self.client.connect(self.connectDetails)
         print("Connected to the Tracker Successfully")
        except:
            print("Connection Failed")

    def trackerClient(self):
        try:
            self.client.send(self.message)
            print("message send")
            status = self.client.recv(4096).decode('utf-8')
            try:
                if(status[4]=="R"):
                    print(status)
                    extracted = RequestConnectedExtraction(status)
                    print("extracteddata",type(extracted.extraction()))
                    peerDetailsTable = PeerDetailsTable()
                    peerDetailsTable.addMultiple(extracted.extraction())

            except:
                print("Status of the Message :", status)

        except:
            print("Connection to the tracker failed to some reason")

    def trackerReceiver(self):
        print("conncetdd")
        s = self.client.recv(1024).decode('utf-8')
        print(s)
