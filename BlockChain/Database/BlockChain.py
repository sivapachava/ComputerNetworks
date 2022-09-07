import sqlite3


class BlockChainDT:
    def __init__(self):
        pass

    def createBlockChainTable(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE BlockChain (
            SequenceNumber INTEGER PRIMARY KEY NOT NULL,
            Hash TEXT (20) NOT NULL,
            Version TEXT (20) NOT NULL,
            PreviousHash TEXT (20) NOT NULL,
            MerkelRoot TEXT (20) NOT NULL,
            TimeStamp TEXT (20) NOT NULL,
            DifficultyTarget TEXT (20) NOT NULL,
            Nonce INTEGER,
            TransactionCounter INTEGER,
            Transactions TEXT (20) NOT NULL);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addBlocks(self, data):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into BlockChain (Hash,Version,PreviousHash,MerkelRoot,TimeStamp,DifficultyTarget,Nonce,TransactionCounter,Transactions) values(?,?,?,?,?,?,?,?,?);"
        #try:
        cur = db.cursor()
        cur.execute(qry, data)
        db.commit()
        print("new transactions added to the database successfully")
        #except:
           #print("error in operation")
           #db.rollback()
        db.close()

    def addMultiple(self,datas):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = "insert into peerData (Hash,Version,PreviousHash,MerkelRoot,TimeStamp,DifficultyTarget,Nonce,TransactionCounter,Transactions) values(?,?,?,?,?,?,?,?,?);"
        try:
            for data in datas:
              cur = db.cursor()
              cur.execute(qry,data)
              db.commit()
              print("new peer details added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def retriveBlock(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select * FROM BlockChain """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

#get the last stored hash from the database
    def retriveLastHash(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """ SELECT Hash FROM BlockChain ORDER BY SequenceNumber DESC LIMIT 1 ; """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchone()
            db.close()
            return result

        except:
            print("error in operation")

    def retrieveBlockVaidation(self):
        db = sqlite3.connect('./Database/BlockChain.db')
        qry = """select SequenceNumber,Hash FROM BlockChain """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            db.close()
            return result
        except:
            print("error in operation")

