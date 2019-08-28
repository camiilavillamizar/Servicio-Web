from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database/bd.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'mysecretkey'

@app.route("/", methods=['GET'])
def inicio():
    return render_template('inicio.html')

@app.route("/users/list",  methods=['GET'])
def lista():
    estudiantes = db.engine.execute("SELECT * FROM users")
    return render_template('lista.html', data=estudiantes)

@app.route('/api/v1/users/')
def tres():
    data= db.engine.execute('select * from users')
    return jsonify({'Listado': [dict(row) for row in data]})
if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)