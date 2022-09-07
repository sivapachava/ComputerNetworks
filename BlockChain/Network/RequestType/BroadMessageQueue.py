from BlockChain.Database.MessageQueue import MessageQueue
import socket

class BroadMessageQueue:
    def __init__(self,connectDetails,message,id):
        self.connectDetails = connectDetails
        self.message = message
        self.id = id

    def sPeer(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(10)
        try:
            client.connect(self.connectDetails)
            client.settimeout(None)
            client.send(self.message)
            status = client.recv(1024).decode('utf-8')
            print("Status of the Message :", status)
            messageQueue = MessageQueue()
            messageQueue.deleteMessage(self.id)
            print("One Queue cleared")
        except:
            print(self.connectDetails)


