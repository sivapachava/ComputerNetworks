import sqlite3

class MiningCompleteStatusDT:
    def __init__(self):
        pass

    def createTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE MiningCompleteStatus (
            Status1 TEXT (20) NOT NULL ,
            Status2 INTEGER );''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addMiningStatus(self,data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into MiningCompleteStatus (Status1,Status2) values(?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("new transactions added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def retriveMiningStatus(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select * FROM MiningCompleteStatus """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

    def deleteMiningStatus(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """ delete FROM MiningCompleteStatus """
        try:
            cur = db.cursor()
            cur.execute(qry)
            db.commit()
            db.close()
            print("Data Successfully deleted")
        except:
            print("error in operation")