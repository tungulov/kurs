from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.modules.find_user_in_db import find_user_in_db


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
        sql_statement = provider.get(
            'find_internal_user.sql',
            {'login': login, 'password': password}
        )
        user = find_user_in_db(db_config, sql_statement)
        if not user: 
            return render_template('auth_login.html', error = "неправильный логин и/или пароль")
        
        session['user_id'] = user['user_id']
        session['user_group'] = user['user_group']
        session['role'] = user['role']
        session.permanent = True
        return redirect('/')


