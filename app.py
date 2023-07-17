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
      cursor.execute(querys.CREATE_DEPARTAMENTS_TABLE)
      cursor.execute(querys.SELECT_DEPARTAMENT, (id,))
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


#subject controller

@app.post("/api/subject/create")
def create_subject():
  data = request.get_json()
  name = data["name"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_SUBJECTS_TABLE)
          cursor.execute(querys.INSERT_SUBJECT, (name,))
  return {"message": "subject created!"}, 201

@app.get("/api/subjects")
def index_subjects():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_SUBJECTS_TABLE)
        cursor.execute(querys.SELECT_SUBJECTS)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/subject/<int:id>")
def get_subject(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_SUBJECTS_TABLE)
      cursor.execute(querys.SELECT_SUBJECT, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/subject/update/<int:id>")
def update_subject(id: "int"):
  data = request.get_json()
  name = data["name"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_SUBJECTS_TABLE)
      cursor.execute(querys.UPDATE_SUBJECT, (name, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/subject/delete/<int:id>")
def delete_subject(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_SUBJECTS_TABLE)
      cursor.execute(querys.DELETE_SUBJECT, (id,))
  return {"message": "subject deleted!"}, 200

#class controller

@app.post("/api/class/create")
def create_class():
  data = request.get_json()
  name = data["name"]
  teacher_id = data["teacher_id"]
  subject_id = data["subject_id"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_CLASSES_TABLE)
          cursor.execute(querys.INSERT_CLASS, (name,teacher_id, subject_id))
  return {"message": "class created!"}, 201

@app.get("/api/classes")
def index_class():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_CLASSES_TABLE)
        cursor.execute(querys.SELECT_CLASSES)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/class/<int:id>")
def get_class(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_CLASSES_TABLE)
      cursor.execute(querys.SELECT_CLASS, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/class/update/<int:id>")
def update_class(id: "int"):
  data = request.get_json()
  name = data["name"]
  teacher_id = data["teacher_id"]
  subject_id = data["subject_id"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_CLASSES_TABLE)
      cursor.execute(querys.UPDATE_CLASS, (name, teacher_id, subject_id, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/class/delete/<int:id>")
def delete_class(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_CLASSES_TABLE)
      cursor.execute(querys.DELETE_CLASS, (id,))
  return {"message": "class deleted!"}, 200


#comment controller

@app.post("/api/comment/create")
def create_comment():
  data = request.get_json()
  content = data["content"]
  grade = data["grade"]
  user_id = data["user_id"]
  teacher_id = data["teacher_id"]
  class_id = data["class_id"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_COMMENTS_TABLE)
          cursor.execute(querys.INSERT_COMMENT, (content, grade ,user_id ,teacher_id, class_id))
  return {"message": "comment created!"}, 201

@app.get("/api/comments")
def index_comment():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_COMMENTS_TABLE)
        cursor.execute(querys.SELECT_COMMENTS)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/comment/<int:id>")
def get_comment(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMMENTS_TABLE)
      cursor.execute(querys.SELECT_COMMENT, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/comment/update/<int:id>")
def update_comment(id: "int"):
  data = request.get_json()
  content = data["content"]
  grade = data["grade"]
  user_id = data["user_id"]
  teacher_id = data["teacher_id"]
  class_id = data["class_id"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMMENTS_TABLE)
      cursor.execute(querys.UPDATE_COMMENT, (content, grade ,user_id ,teacher_id, class_id, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/comment/delete/<int:id>")
def delete_comment(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMMENTS_TABLE)
      cursor.execute(querys.DELETE_COMMENT, (id,))
  return {"message": "comment deleted!"}, 200


#complaint controller

@app.post("/api/complaint/create")
def create_complaint():
  data = request.get_json()
  status = data["status"]
  user_id = data["user_id"]
  comment_id = data["comment_id"]
  with connection:
      with connection.cursor(cursor_factory=RealDictCursor) as cursor:
          cursor.execute(querys.CREATE_COMPLAINTS_TABLE)
          cursor.execute(querys.INSERT_COMPLAINT, (status, user_id, comment_id))
  return {"message": "complaint created!"}, 201

@app.get("/api/complaints")
def index_complaint():
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(querys.CREATE_COMPLAINTS_TABLE)
        cursor.execute(querys.SELECT_COMPLAINTS)
        data = cursor.fetchall()
  return data, 200


@app.get("/api/complaint/<int:id>")
def get_complaint(id: "int"):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMPLAINTS_TABLE)
      cursor.execute(querys.SELECT_COMPLAINT, (id,))
      data = cursor.fetchone()
  return data, 200

@app.patch("/api/complaint/update/<int:id>")
def update_complaint(id: "int"):
  data = request.get_json()
  status = data["status"]
  user_id = data["user_id"]
  comment_id = data["comment_id"]
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMPLAINTS_TABLE)
      cursor.execute(querys.UPDATE_COMPLAINT, (status, user_id, comment_id, id))
      data = cursor.fetchall()[0]
  return data, 200


@app.delete("/api/complaint/delete/<int:id>")
def delete_complaint(id: int):
  with connection:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(querys.CREATE_COMPLAINTS_TABLE)
      cursor.execute(querys.DELETE_COMPLAINT, (id,))
  return {"message": "complaint deleted!"}, 200