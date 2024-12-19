from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.access import admin_required
from src.modules.admin_module import call_procedure
from src.modules.record_module import record_module_get_ships


admin_blueprint = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates'
)


@admin_blueprint.route('/admin', methods=['GET', 'POST'])
@admin_required
def report_handler():
    if request.method == 'GET':
        return render_template('admin_report.html', error = "")
    else:
        month = request.form.get('month', '')
        year = request.form.get('year', '')
        sql_statement = provider.get(
            'use_procedure.sql',
            {'month': month, 'year': year}
        )
        render_data = call_procedure(db_config, sql_statement)
       
        return render_template('admin_report.html', render_data=render_data)


@admin_blueprint.route('/admin/ship', methods=['GET', 'POST'])
@admin_required
def ship_adding_handler():
    if request.method == 'POST':
        pass
        # month = request.form.get('month', '')
        # year = request.form.get('year', '')
        # sql_statement = provider.get(
        #     'use_procedure.sql',
        #     {'month': month, 'year': year}
        # )
        # render_data = call_procedure(db_config, sql_statement)
       
        # return render_template('admin_report.html', render_data=render_data)
    
    ships = record_module_get_ships()
    return render_template('add_ship.html', ships=ships)

@admin_blueprint.route('/no_admin', methods=['GET', 'POST'])
def no_admin_handler():
    return render_template('no_admin.html')
   