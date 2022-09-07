import time
from BlockChain.Database.MessageQueue import MessageQueue
from BlockChain.Network.RequestType.BroadMessageQueue import BroadMessageQueue


class MessageQueueLogic:
    def __init__(self):
        pass

    def messageQueuing(self):
        while True:
            print("Message Queue Wait")
            time.sleep(60)
            print("Message Queue Started")
            messageQueue = MessageQueue()
            messages = messageQueue.retriveMessageQueue("192.168.0.13")
            print("message Queues:", messages)
            for message in messages:
                print("Current Queue details",message[0],message[1],message[2],message[3])
                broadMessageQueue = BroadMessageQueue((message[2], message[3]), message[1], message[0])
                print(type((message[2], message[3])))
                broadMessageQueue.sPeer()
