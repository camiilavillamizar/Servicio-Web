from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, static_url_path='/static')

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
l=listaC()

lis=l.t
lista1=lista.t

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
    
    
if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)