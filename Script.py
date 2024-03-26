from fastapi import FastAPI
import sqlite3

app = FastAPI()

class sql_handle:
    def __init__(self,id : str,amount : str,name : str,log : str):
        self.id = id
        self.amount = amount
        self.name  = name
        self.log = log

    @staticmethod
    def create_Table():
        conn = sqlite3.connect("data.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS user (
                    name TEXT NOT NULL,
                    id TEXT NOT NULL,
                    log TEXT NOT NULL,
                    amount TEXT NOT NULL
                    )
                    """)
        conn.close()

    @staticmethod
    def find_user(name:str):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE name = ?",(name,))
        records = cursor.fetchone()
        conn.close()
        cursor.close()
        return bool(records)

    @staticmethod
    def payment_addresss(name:str,id:str):
        if sql_handle.find_user(name=name):
            conn = sqlite3.connect("data.db")
            conn.execute("INSERT INTO data (id) SELECT ? WHERE name = ?",(id,name))
            conn.close()
        else:
            return "User not found"
        
    @staticmethod
    def add_payment_log(name:str,log:str):
        if sql_handle.find_user(name=name):
            conn = sqlite3.connect("data.db")
            conn.execute("INSERT INTO data (log) SELECT ? WHERE name = ?",(log,name))
            conn.close()
        else:
            return "User not found"
        
    def add_payment_balance(amount:str,name:str):
        conn = sqlite3.connect("data.db")
        conn.execute("INSERT INTO data (amount) SELECT ? WHERE name = ?",(amount,name))
        conn.close()

    def register_user(self):
        conn = sqlite3.connect("data.db")
        conn.execute("INSERT INTO data (amount) SELECT ? WHERE name = ?",(amount,name))
        conn.close()

@app.get("/",status_code=200)
def index():
    return "200 ok"

@app.post("/send-payment")
def send_payment(id:str,amount:int,name:str):
    pass

@app.get("/revice-payment")
def revice_Payment():
    pass