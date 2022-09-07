# post request to the single peer

import socket

class BroadCastSelected:
    def __init__(self,connectDetails,message):
        self.connectDetails = connectDetails
        self.message = message

    def sPeer(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        try:
            client.connect(self.connectDetails)
            client.settimeout(None)
            client.send(self.message)
            status = client.recv(1024).decode('utf-8')
            print("Status of the Message :", status)
        except:
            print("Sending Failed")
