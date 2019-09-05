from app import app
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database/bd.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'
db=SQLAlchemy(app)


class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance


class listaC(Singleton):
     t=[]
     datos= db.engine.execute('select * from users;')
     for row in datos:
          t.append(row)    


lista=listaC()
lista1=lista.t
l=listaC()
lis=l.t