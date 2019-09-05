from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json



app = Flask(__name__, static_url_path='/static')



from vistas import *
    
    
if __name__ == "__main__":
    app.run(debug= True)