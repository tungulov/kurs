import os

from flask import Flask, render_template, session

from src.auth.routes import auth_blueprint
from src.admin.routes import admin_blueprint
from src.brigadir.routes import brigadir_blueprint
from src.access import login_required


app = Flask(__name__)
app.secret_key = 'my_super_secret_key'
app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(brigadir_blueprint)

@app.route('/', methods=['GET', 'POST'])
@login_required
def hello():    
    role = session['role']
    return render_template('menu.html', role=role)


@app.route('/logout')
def logout_handler():
    session.clear()
    return render_template('logout.html')


def start():
    app.run(host='127.0.0.1', port=int(os.getenv('BACKEND_PORT')))
