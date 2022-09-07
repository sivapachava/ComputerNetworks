import sqlite3

class MessageQueue:
    def __init__(self):
        pass

    def createMessageTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE MessageQueue (
            SequenceNumber INTEGER PRIMARY KEY NOT NULL,
            Message TEXT (20) NOT NULL, 
            peerIPAddress TEXT (20) NOT NULL, 
            peerPort INTEGER);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addMessageQueue(self, data):

        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into MessageQueue (Message,peerIPAddress,peerPort) values(?,?,?);"
        try:
           cur = db.cursor()
           cur.execute(qry, data)
           db.commit()
           db.close()
           print("new message queue added to the database successfully")
        except:
           print("error in operation")


    def retriveMessageQueue(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select * FROM MessageQueue """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")
