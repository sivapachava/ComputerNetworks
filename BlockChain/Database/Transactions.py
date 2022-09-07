
import sqlite3
class TransactionsDT:
    def __init__(self):
        pass

    def createTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE Transactions (
            DateAndTime TEXT (20) NOT NULL,
            TransactionID TEXT (20) NOT NULL,
            SenderName TEXT (20) NOT NULL,
            AmountMessage TEXT (20) NOT NULL,
            DigitalSignature TEXT (20) NOT NULL );''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addElements(self,data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into Transactions (DateAndTime, TransactionID,SenderName,AmountMessage,DigitalSignature) values(?,?,?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("new transactions added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()