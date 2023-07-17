# Description

Projeto de Disciplina Banco de Dados.
Elaborar um sistema onde estudantes possam avaliar professores e disciplinas. Permitir que estudantes se cadastrem e postem avaliações de professores e turmas de diferentes semestres.

### aluno

- Gabriel Cruz Vaz Santos - 200049038

# Install Dependencies

To run this project you will need

- pip
- python
- postgresql
- flask

# Before Project Run

You will need to create a database in your postgresql using command line

- Open command line and type:

`sudo -i -u <yourpostgreusername>`

`sudo -u <yourpostgresusername> psql`

it will require your role password to proceed.

## If first time running project run:

`create database avaliacao_disciplida_db;`

then run to connect to the database. Do not close the process!

`\c avaliacao_disciplina_db`

After connecting to the database you can run to check which postgres user is connected to the db.
This will be important when setting ours environment variables.

`\conninfo`

# Run Project

In the project directory, you can run:

### `git pull`

### `pipenv shell`

- After running this command, make sure you are using the correct python interpreter

### `pipenv install -r requirements.txt`

### Create a .env file

in .env file code:

```py
DATABASE_USERNAME = "your postgresqlRoleName"
DATABASE_PASSWORD = "your postgresqlRolePassword"
```

### `flask run`

# References

- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04
- https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application -https://blog.teclado.com/first-rest-api-flask-postgresql-python/
