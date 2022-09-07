import sqlite3

class PeerData:
    def __init__(self):
        pass

    def createPeerDataTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE PeerName (
            SequenceNumber INTEGER PRIMARY KEY NOT NULL,
            Name TEXT (20) NOT NULL, 
            peerIPAddress TEXT (20) NOT NULL, 
            peerPort INTEGER);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addPeerData(self, data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into PeerName (Name,peerIPAddress,peerPort) values(?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("User Created Successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def retrivePeerData(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select * FROM PeerName """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")
