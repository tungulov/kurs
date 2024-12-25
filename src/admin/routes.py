from flask import Blueprint, request, render_template, session, redirect
from src.access import admin_required
from src.admin.ship.routes import admin_ships_blueprint

admin_blueprint = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)

admin_blueprint.register_blueprint(admin_ships_blueprint)

@admin_blueprint.route('/', methods=['GET', 'POST'])
@admin_required
def admin_handler():
    return redirect('/admin/ship')

@admin_blueprint.route('/no_admin', methods=['GET', 'POST'])
def no_admin_handler():
    return render_template('no_admin.html')