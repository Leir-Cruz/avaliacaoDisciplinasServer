# Create Tables

CREATE_USERS_TABLE = '''CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email varchar(250) NOT NULL,
  password varchar(250) NOT NULL,
  code varchar(250) NOT NULL,
  graduation varchar(250) NOT NULL,
  isAdmin boolean
  ); '''

CREATE_DEPARTAMENTS_TABLE = '''CREATE TABLE IF NOT EXISTS departaments (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL
  ); '''

CREATE_TEACHERS_TABLE = '''CREATE TABLE IF NOT EXISTS teachers (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  FOREIGN KEY(departament_id) REFERENCES departaments(id) ON DELETE CASCADE
  ); '''


CREATE_SUBJECTS_TABLE = '''CREATE TABLE IF NOT EXISTS subjects (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL
  ); '''


CREATE_CLASSES_TABLE = '''CREATE TABLE IF NOT EXISTS classes (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE NOT NULL,
  FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE NOT NULL
  ); '''

CREATE_COMMENTS_TABLE = '''CREATE TABLE IF NOT EXISTS comments (
  id SERIAL PRIMARY KEY,
  content text NOT NULL,
  grade integer NOT NULL,
  FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE NOT NULL,
  FOREIGN KEY(class_id) REFERENCES classes(id) ON DELETE CASCADE NOT NULL
  ); '''

CREATE_COMPLAINT_TABLE = '''CREATE TABLE IF NOT EXISTS complaints (
  id SERIAL PRIMARY KEY,
  status varchar(250) NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE NOT NULL,
  FOREIGN KEY(comment_id) REFERENCES comments(id) ON DELETE CASCADE NOT NULL
  ); '''

# Insert Querys
INSERT_USER = '''INSERT INTO users (email, password, code, graduation, isAdmin) VALUES (%s, %s, %s, %s, %s);'''
INSERT_DEPARTAMENT = '''INSERT INTO departaments (name) VALUES (%s);'''
INSERT_TEACHER = '''INSERT INTO teachers (name, departament_id) VALUES (%s, %s);'''
INSERT_SUBJECT = '''INSERT INTO subjects (name) VALUES (%s);'''
INSERT_CLASS = '''INSERT INTO classes (name, teacher_id, subject_id) VALUES (%s, %s, %s);'''
INSERT_COMMENT = '''INSERT INTO comments (content, grade, user_id, teacher_id, class_id) VALUES (%s, %d, %s, %s, %s);'''
INSERT_COMPLAINT = '''INSERT INTO complaints (status, user_id, comment_ud) VALUES (%s, %s, %s);'''

#Select all Querys
SELECT_USERS = '''SELECT * FROM users;'''
SELECT_DEPARTAMENTS = '''SELECT * FROM departaments;'''
SELECT_TEACHERS = '''SELECT * FROM teachers;'''
SELECT_CLASSES = '''SELECT * FROM classes;'''
SELECT_COMMENTS = '''SELECT * FROM teachers WHERE teacher_id=%s OR class_id=%s;'''

#Select one Querys
LOGIN = '''SELECT email FROM users WHERE email=%s AND password=%s LIMIT 1;'''
SELECT_USER = '''SELECT * FROM users WHERE id=%s LIMIT 1;'''

# Update Querys
UPDATE_USER = '''UPDATE users SET email=%s, password=%s, code=%s, graduation=%s WHERE id=%s RETURNING *;'''

# Delete Querys
DELETE_USER = '''DELETE FROM users WHERE id=%s;'''

