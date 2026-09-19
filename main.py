import os
from fastapi import FastAPI
from pydantic import BaseModel
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

api = FastAPI()

class TaskRequest(BaseModel):
    id: int
    title: str
    status: bool
 

@api.get("/")
def home():
    return "This is home page."

def connect_mysql():
    conn = connect(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME")
    )

    penn = conn.cursor()
    return conn, penn



@api.post("/create")
def add_task(request:TaskRequest):
    id = request.id
    title = request.title
    status = request.status
    conn,penn = connect_mysql()
    penn.execute("insert into task(id, title, status) values (%s, %s, %s)", (id, title, status))
    conn.commit()
    conn.close()
    print(request)
    return "Task added successfully"



