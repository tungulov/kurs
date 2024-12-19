from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.modules.auth_module import auth_module


auth_blueprint = Blueprint(
    'auth_bp',
    __name__,
    template_folder='templates'
)


@auth_blueprint.route('/auth', methods=['GET', 'POST'])
def login_handler():
    if request.method == 'GET':
        return render_template('auth_login.html')
    else:
        login = request.form.get('login', '')
        password = request.form.get('password', '')
        
        is_authed = auth_module(login, password,)
        if not is_authed: 
            return render_template('auth_login.html', error = "неправильный логин и/или пароль")
        
        return redirect('/')


