from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database/bd.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'mysecretkey'

#vista de inicio
@app.route("/", methods=['GET'])
def inicio():
    return render_template('inicio.html')

#Parte donde se despliega la lista de estudiantes de la base datos
@app.route("/users/list", methods=['GET'])
def lista():
    estudiantes = db.engine.execute("SELECT * FROM users")
    return render_template('lista.html', data=estudiantes)

#API donde devuelve el Json
@app.route('/api/v1/users/',methods=['GET'])
def tres():
    resultado= db.engine.execute('SELECT * FROM users')
    return jsonify({'Json': [dict(row) for row in resultado]})

if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)