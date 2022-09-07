import sqlite3

class CreateDatabase:
    def __init__(self):
        try:
            connection = sqlite3.connect('./Tracker/DatabaseSource/Tracker.db')
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                        (Title TEXT, Director TEXT, Year INT)''')
            connection.commit()
            connection.close()

        except:
            print("database creation failed")




