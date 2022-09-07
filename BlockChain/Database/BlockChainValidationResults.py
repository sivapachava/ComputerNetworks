import sqlite3

class BlockChainValidation:
    def __init__(self):
        pass

    def createBlockChainValidation(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE BlockChainValidation (
            BlockSequenceNumber INTEGER,
            Status TEXT (20) NOT NULL 
            );''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addBlockChainValidation(self, data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into BlockChainValidation (BlockSequenceNumber,Status) values(?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("User Created Successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()
