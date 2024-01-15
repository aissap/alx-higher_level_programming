0x0F-python-object_relational_mapping

Before You Start…
Please make sure your MySQL server is in version 8.0.

How to install MySQL 8.0 in Ubuntu 20.04
Background Context
In this project, you will link two amazing worlds: Databases and Python!

Part 1: MySQLdb Module
You will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

Without ORM:

python
Copy code
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
Part 2: SQLAlchemy (Object Relational Mapper - ORM)
You will use the module SQLAlchemy to abstract the storage to the usage.

With an ORM:

python
Copy code
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
Do you see the difference? Cool, right?

The Biggest Difficulty with ORM: The Syntax!
All ORMs have similar syntax but not always the same. Read tutorials and jump into it if you don't get something.

Resources
Read or watch:

Object-relational mappers
mysqlclient/MySQLdb documentation
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers
SQLAlchemy Tutorial
Python Virtual Environments: A primer
Learning Objectives
At the end of this project, you are expected to be able to explain:

General
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks yourself to meet the learning objectives.
No copying and pasting someone else’s work.
Not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Executed with MySQLdb version 2.0.x
Executed with SQLAlchemy version 1.4.x
All files end with a new line
First line of all files: #!/usr/bin/python3
Mandatory README.md file at the root of the folder
Code uses pycodestyle (version 2.8.*)
All files must be executable
Length of files will be tested using wc
All modules, classes, and functions have documentation
Not allowed to use execute with SQLAlchemy
Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, install venv:

bash
Copy code
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

bash
Copy code
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x
bash
Copy code
$ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy._version_ 
'1.4.22'
Also, you can have this warning message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")

MySQL Installation
Link to MySQL Installation Guide

ORM Introduction
Link to Object-relational mappers Introduction

MySQLdb Documentation
Link to mysqlclient/MySQLdb documentation

MySQLdb Tutorial
Link to MySQLdb tutorial

SQLAlchemy Tutorial
Link to SQLAlchemy tutorial

SQLAlchemy
Link to SQLAlchemy

SQLAlchemy Introduction
Link to Introduction to SQLAlchemy

Flask SQLAlchemy
Link to Flask SQLAlchemy

SQLAlchemy Stumbling Blocks
Link to 10 common stumbling blocks for SQLAlchemy newbies

SQLAlchemy Cheatsheet
Link to Python SQLAlchemy Cheatsheet

SQLAlchemy Tutorial (PostgreSQL)
Link to SQLAlchemy ORM Tutorial for Python Developers (PostgreSQL)

SQLAlchemy Tutorial (General)
Link to SQLAlchemy Tutorial (General)

Python Virtual Environment
Link to Python Virtual Environments: A primer
