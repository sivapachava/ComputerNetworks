import sqlite3


class RegisteredPeerTable:
    def __init__(self):
        pass

    def createRegisteredTable(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE RegisteredPeers (  
            Name TEXT (20) NOT NULL,      
            peerIPAddress TEXT (20) NOT NULL,
            peerPort INTEGER,
            peerPublicKey TEXT (20) NOT NULL);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addRegisteredElements(self,data):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = "insert into RegisteredPeers (name,peerIPAddress,peerPort,peerPublicKey) values(?,?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("new peer details added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    #retrive all ipaddress and port number
    def retrieveRegisteredElements(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select peerIPAddress , peerPort FROM RegisteredPeers """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

    def retreieveRegisteredPeerName(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select peerName FROM RegisteredPeers """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")


    def retrieveRegisteredAllSelected(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select * FROM RegisteredPeers """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

    def deleteRegisteredPeerData(self,connection):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """delete FROM RegisteredPeers where peerIPAddress = ? """
        try:
           print("conencccdcdcdcdc",connection[0])
           cur = db.cursor()
           cur.execute(qry,(connection[0],))
           db.commit()
           db.close()
           print("Successfully deleted")
        except:
           print("error in operation")



