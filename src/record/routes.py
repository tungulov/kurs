from flask import Blueprint, request, render_template, session, redirect
from src.connection import DBConnection, db_config, provider

from src.modules.record_module import record_module_get_ships, record_module_add_record

record_blueprint = Blueprint(
    'record_bp',
    __name__,
    template_folder='templates'
)

@record_blueprint.route('/record', methods=['GET', 'POST'])
def ships():
    if request.method == 'POST':
        record_module_add_record(request.form.get('ship_id'), session['user_id'])
        return redirect('/')

    ships = record_module_get_ships()
    return render_template('add_record.html', ships=ships)