import sqlite3

class TransactionsLedgerDT:
    def __init__(self):
        pass

    def createLedgerTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE TransactionLedger (
            DateAndTime TEXT (20) NOT NULL,
            TransactionID TEXT (20) NOT NULL,
            SenderName TEXT (20) NOT NULL,
            ReceiverName TEXT (20) NOT NULL,
            Amount TEXT (20) NOT NULL,
            Message TEXT (20) NOT NULL );''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addLedgerElements(self,data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into TransactionLedger (DateAndTime, TransactionID,SenderName,ReceiverName,Amount,Message) values(?,?,?,?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("new transactions added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def retriveLedgerElement(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select * FROM TransactionLedger """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

    def deleteLedgerElement(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """ delete FROM TransactionLedger """
        try:
            cur = db.cursor()
            cur.execute(qry)
            db.commit()
            db.close()
            print("Data Successfully deleted")
        except:
            print("error in operation")