import sqlite3


class PeerDetailsTable:
    def __init__(self):
        pass

    def createTable(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE peerData (
            Name TEXT (20) NOT NULL,     
            peerIPAddress TEXT (20) NOT NULL,
            peerPort INTEGER,
            peerPublicKey TEXT (20) NOT NULL);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addElements(self,data):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = "insert into peerData (Name,peerIPAddress,peerPort,peerPublicKey) values(?,?,?,?);"
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
    def retrieveElements(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select peerIPAddress , peerPort FROM peerData """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

        # retrive all ipaddress and port number


    def retreievePeerName(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select peerName FROM peerData """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")


    def retrieveAllSelected(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """select * FROM peerData"""
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

    def deletePeerData(self,connection):
        db = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
        qry = """delete FROM peerData where peerIPAddress = ? """
        try:
           print("conencccdcdcdcdc",connection[0])
           cur = db.cursor()
           cur.execute(qry,(connection[0],))
           db.commit()
           db.close()
           print("Successfully deleted")
        except:
           print("error in operation")



