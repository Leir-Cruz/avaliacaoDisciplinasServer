import os
import psycopg2
from psycopg2.extras import RealDictCursor
import querys
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
#create flask api
app = Flask(__name__)
CORS(app)

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
  isadmin = data["isadmin"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_USERS_TABLE)
          cursor.execute(querys.INSERT_USER, (email, password,code, graduation, isadmin))
  return {"message": "User created!"}, 201

@app.get("/api/users")
def index_users():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_USERS_TABLE)
        cursor.execute(querys.SELECT_USERS)
        data = cursor.fetchall()
  return  data, 200

@app.post("/api/login")
def login():
  data = request.get_json()
  email = data["email"]
  password = data["password"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_USERS_TABLE)
        cursor.execute(querys.LOGIN, (email, password))
        data = cursor.fetchone()
  return data, 200

@app.get("/api/user/<int:id>")
def get_user(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.SELECT_USER, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/user/update/<int:id>")
def update_user(id: "int"):
  data = request.get_json()
  email = data["email"]
  password = data["password"]
  code = data["code"]
  graduation = data["graduation"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.UPDATE_USER, (email, password, code, graduation, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/user/delete/<int:id>")
def delete_user(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.DELETE_USER, (id,))
  return {"message": "user deleted!"}, 200

#departament controller

@app.post("/api/departament/create")
def create_departament():
  data = request.get_json()
  name = data["name"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_DEPARTAMENTS_TABLE)
          cursor.execute(querys.INSERT_DEPARTAMENT, (name,))
  return {"message": "departament created!"}, 201

@app.get("/api/departaments")
def index_departaments():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_DEPARTAMENTS_TABLE)
        cursor.execute(querys.SELECT_DEPARTAMENTS)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/departament/<int:id>")
def get_departament(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_USERS_TABLE)
      cursor.execute(querys.SELECT_USER, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/departament/update/<int:id>")
def update_departament(id: "int"):
  data = request.get_json()
  name = data["name"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_DEPARTAMENTS_TABLE)
      cursor.execute(querys.UPDATE_DEPARTAMENT, (name, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/departament/delete/<int:id>")
def delete_departament(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_DEPARTAMENTS_TABLE)
      cursor.execute(querys.DELETE_DEPARTAMENT, (id,))
  return {"message": "departament deleted!"}, 200



#teacher controller

@app.post("/api/teacher/create")
def create_teacher():
  data = request.get_json()
  name = data["name"]
  departament_id = data["departament_id"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_TEACHERS_TABLE)
          cursor.execute(querys.INSERT_TEACHER, (name, departament_id))
  return {"message": "teacher created!"}, 201

@app.get("/api/teachers")
def index_teachers():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_TEACHERS_TABLE)
        cursor.execute(querys.SELECT_TEACHERS)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/teacher/<int:id>")
def get_teacher(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_TEACHERS_TABLE)
      cursor.execute(querys.SELECT_TEACHER, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/teacher/update/<int:id>")
def update_teacher(id: "int"):
  data = request.get_json()
  name = data["name"]
  departament_id = data["departament_id"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_TEACHERS_TABLE)
      cursor.execute(querys.UPDATE_TEACHER, (name,departament_id ,id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/teacher/delete/<int:id>")
def delete_teacher(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_TEACHERS_TABLE)
      cursor.execute(querys.DELETE_TEACHER, (id,))
  return {"message": "teacher deleted!"}, 200


