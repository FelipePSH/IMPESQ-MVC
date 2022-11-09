from flask import Flask, render_template
from flaskext.mysql import MySQL



app = Flask(__name__)


mysql = MySQL()
app.config.from_object('config')
mysql.init_app(app)
