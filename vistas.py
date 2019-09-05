from app import app
from modelo import lista1,lis
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


@app.route("/", methods=['GET'])
def inicio():
    return render_template('inicio.html')

@app.route("/users/list",  methods=['GET'])
def lista_vista():
    print (hex(id(lista1)))
    return render_template('lista.html', data=lista1)

@app.route('/api/v1/users/')
def tres():
     print (hex(id(lis)))
     data=lis
     otrcosa=json.dumps({'Json': [dict(row) for row in data]})
     f=open('archivo.json','w')
     f.write(otrcosa)
     return render_template('inicio.html')
     f.close()