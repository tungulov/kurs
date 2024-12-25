from functools import wraps

from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:            
            return func(*args, **kwargs)
        return redirect(url_for('auth_bp.login_handler'))
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role' in session and session['role'] == 'admin':
            return func(*args, **kwargs)
        return redirect(url_for('admin_bp.no_admin_handler'))
    return wrapper


def brigadir_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role' in session and (session['role'] == 'brigadir' or session['role'] == 'admin'):
            return func(*args, **kwargs)
        return redirect(url_for('brigadir_bp.no_brigadir_handler'))
    return wrapper

