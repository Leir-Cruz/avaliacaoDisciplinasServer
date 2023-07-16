import os
import psycopg2
from psycopg2.extras import RealDictCursor
import querys
from flask import Flask, request
from dotenv import load_dotenv

#create flask api
app = Flask(__name__)

#getting ours enviromment variables
load_dotenv()
sqlUser = os.getenv("DATABASE_USERNAME")
sqlPassword = os.getenv( "DATABASE_PASSWORD")

# Connect to the database
connection = psycopg2.connect(database="avaliacao_disciplina_db", user=sqlUser, password=sqlPassword, host="localhost", port="5432")

#user controller
@app.post("/api/user/create")
def create():
  data = request.get_json()
  email = data["email"]
  password = data["password"]
  code = data["code"]
  graduation= data["graduation"]
  isAdmin = data["isAdmin"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_USERS_TABLE)
          cursor.execute(querys.INSERT_USER, (email, password,code, graduation, isAdmin))
  return {"message": "User created!"}, 201

@app.get("/api/users")
def index():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_USERS_TABLE)
        cursor.execute(querys.SELECT_USERS)
        data = cursor.fetchall()
  return {"message": "all users sended!", "data": data}, 200

@app.get("/api/login")
def login():
  data = request.get_json()
  email = data["email"]
  password = data["password"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_USERS_TABLE)
        cursor.execute(querys.LOGIN, (email, password))
        data = cursor.fetchone()
  return {"message": "loggedUser!", "data": data}, 200

@app.get("/api/user/<int:id>")
def getOne(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.SELECT_USER, (id,))
      data = cursor.fetchone()
  return {"message": "user returned", "data": data}, 200

@app.patch("/api/user/update/<int:id>")
def update(id: "int"):
  data = request.get_json()
  email = data["email"]
  password = data["password"]
  code = data["code"]
  graduation = data["graduation"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.UPDATE_USER, (email, password, code, graduation, id))
      data = cursor.fetchall()
  return {"message": "user update", "data": data}, 200


@app.delete("/api/user/delete/<int:id>")
def delete(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.DELETE_USER, (id,))
  return {"message": "user deleted!"}, 200
