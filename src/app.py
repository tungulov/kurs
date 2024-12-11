import os

from flask import Flask, render_template, session
from dotenv import load_dotenv

from src.auth.routes import auth_blueprint
from src.ships.routes import ships_blueprint
from src.admin.routes import admin_blueprint
from src.access import login_required

load_dotenv('.env')

app = Flask(__name__)
app.secret_key = 'my_super_secret_key'
app.register_blueprint(auth_blueprint, url_preefix='/auth')
app.register_blueprint(ships_blueprint, url_preefix='/ships')
app.register_blueprint(admin_blueprint, url_preefix='/admin')


@app.route('/', methods=['GET', 'POST'])
@login_required
def hello():
    return render_template('menu.html')


@app.route('/logout')
def logout_handler():
    session.clear()
    return render_template('logout.html')


def start():
    app.run(host='127.0.0.1', port=int(os.getenv('BACKEND_PORT')))