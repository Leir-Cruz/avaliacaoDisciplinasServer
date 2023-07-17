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
  departament_id integer REFERENCES departaments(id) ON DELETE CASCADE
  ); '''


CREATE_SUBJECTS_TABLE = '''CREATE TABLE IF NOT EXISTS subjects (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL
  ); '''


CREATE_CLASSES_TABLE = '''CREATE TABLE IF NOT EXISTS classes (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  teacher_id integer REFERENCES teachers(id) ON DELETE CASCADE NOT NULL,
  subject_id integer REFERENCES subjects(id) ON DELETE CASCADE NOT NULL
  ); '''

CREATE_COMMENTS_TABLE = '''CREATE TABLE IF NOT EXISTS comments (
  id SERIAL PRIMARY KEY,
  content text NOT NULL,
  grade integer NOT NULL,
  user_id integer REFERENCES users(id) ON DELETE CASCADE NOT NULL,
  teacher_id integer REFERENCES teachers(id) ON DELETE CASCADE,
  class_id integer REFERENCES classes(id) ON DELETE CASCADE 
  ); '''

CREATE_COMPLAINTS_TABLE = '''CREATE TABLE IF NOT EXISTS complaints (
  id SERIAL PRIMARY KEY,
  status varchar(250) NOT NULL,
  user_id integer REFERENCES users(id) ON DELETE CASCADE NOT NULL,
  comment_id integer REFERENCES comments(id) ON DELETE CASCADE NOT NULL
  ); '''

# Insert Querys
INSERT_USER = '''INSERT INTO users (email, password, code, graduation, isAdmin) VALUES (%s, %s, %s, %s, %s);'''
INSERT_DEPARTAMENT = '''INSERT INTO departaments (name) VALUES (%s);'''
INSERT_TEACHER = '''INSERT INTO teachers (name, departament_id) VALUES (%s, %s);'''
INSERT_SUBJECT = '''INSERT INTO subjects (name) VALUES (%s);'''
INSERT_CLASS = '''INSERT INTO classes (name, teacher_id, subject_id) VALUES (%s, %s, %s);'''
INSERT_COMMENT = '''INSERT INTO comments (content, grade, user_id, teacher_id, class_id) VALUES (%s, %s, %s, %s, %s);'''
INSERT_COMPLAINT = '''INSERT INTO complaints (status, user_id, comment_id) VALUES (%s, %s, %s);'''

#Select all Querys
SELECT_USERS = '''SELECT * FROM users;'''
SELECT_DEPARTAMENTS = '''SELECT * FROM departaments;'''
SELECT_TEACHERS = '''SELECT * FROM teachers;'''
SELECT_SUBJECTS = '''SELECT * FROM subjects;'''
SELECT_CLASSES = '''SELECT * FROM classes;'''
SELECT_COMMENTS = '''SELECT * FROM comments;'''
SELECT_COMPLAINTS = '''SELECT * FROM complaints;'''

#Select one Querys
LOGIN = '''SELECT * FROM users WHERE email=%s AND password=%s LIMIT 1;'''
SELECT_USER = '''SELECT * FROM users WHERE id=%s LIMIT 1;'''
SELECT_DEPARTAMENT = '''SELECT * FROM departaments WHERE id=%s LIMIT 1;'''
SELECT_TEACHER = '''SELECT * FROM teachers WHERE id=%s LIMIT 1;'''
SELECT_SUBJECT = '''SELECT * FROM subjects WHERE id=%s LIMIT 1;'''
SELECT_CLASS = '''SELECT * FROM classes WHERE id=%s LIMIT 1;'''
SELECT_COMMENT = '''SELECT * FROM comments WHERE id=%s LIMIT 1;'''
SELECT_COMPLAINT = '''SELECT * FROM complaints WHERE id=%s LIMIT 1;'''


# Update Querys
UPDATE_USER = '''UPDATE users SET email=%s, password=%s, code=%s, graduation=%s WHERE id=%s RETURNING *;'''
UPDATE_DEPARTAMENT = '''UPDATE departaments SET name=%s WHERE id=%s RETURNING *;'''
UPDATE_TEACHER = '''UPDATE teachers SET name=%s, departament_id=%s WHERE id=%s RETURNING *;'''
UPDATE_SUBJECT = '''UPDATE subjects SET name=%s WHERE id=%s RETURNING *;'''
UPDATE_CLASS = '''UPDATE classes SET name=%s, teacher_id=%s, subject_id=%s WHERE id=%s RETURNING *;'''
UPDATE_COMMENT = '''UPDATE comments SET content=%s, grade=%s, user_id=%s, teacher_id=%s, class_id=%s WHERE id=%s RETURNING *;'''
UPDATE_COMPLAINT = '''UPDATE complaints SET status=%s, user_id=%s, comment_id=%s WHERE id=%s RETURNING *;'''

# Delete Querys
DELETE_USER = '''DELETE FROM users WHERE id=%s;'''
DELETE_DEPARTAMENT = '''DELETE FROM departaments WHERE id=%s;'''
DELETE_TEACHER = '''DELETE FROM teachers WHERE id=%s;'''
DELETE_SUBJECT = '''DELETE FROM subjects WHERE id=%s;'''
DELETE_CLASS = '''DELETE FROM classes WHERE id=%s;'''
DELETE_COMMENT = '''DELETE FROM comments  WHERE id=%s;'''
DELETE_COMPLAINT = '''DELETE FROM complaints  WHERE id=%s;'''

