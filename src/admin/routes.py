from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.access import admin_required
from src.modules.ship_module import add_ship, call_procedure, delete_ship, edit_ship, get_ship, get_ships_types, get_ships
from src.common.table_naming import ship_labels

admin_blueprint = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates'
)


@admin_blueprint.route('/admin/ship', methods=['GET'])
@admin_required
def ship_handler():
    ships = get_ships()
    return render_template('ships.html', ships=ships, ship_labels=ship_labels)


@admin_blueprint.route('/admin/ship/add', methods=['GET', 'POST'])
@admin_required
def ship_adding_handler():
    if request.method == 'POST':
        ship_name = request.form.get('ship_name', '')
        tonnage = request.form.get('tonnage', 0)
        home_port = request.form.get('home_port', '')
        ship_type_id = request.form.get('ship_type', 1)
       
        add_ship(ship_name, tonnage, home_port, ship_type_id)
        return redirect('/admin/ship')
           
    ship_types = get_ships_types()
    return render_template('ship_edit.html', ship_types=ship_types, ship=None)


@admin_blueprint.route('/admin/ship/edit/<int:ship_id>', methods=['GET', 'POST'])
@admin_required
def ship_edit_handler(ship_id: int):
    if request.method == 'POST':
        ship_name = request.form.get('ship_name', '')
        tonnage = request.form.get('tonnage', 0)
        home_port = request.form.get('home_port', '')
        ship_type_id = request.form.get('ship_type', 1)
       
        edit_ship(ship_id, ship_name, tonnage, home_port, ship_type_id)
        return redirect('/admin/ship')
    
    ship = get_ship(ship_id)
    ship_types = get_ships_types()
    return render_template('ship_edit.html', ship_types=ship_types, ship=ship)


@admin_blueprint.route('/admin/ship/delete/<int:ship_id>', methods=['GET'])
@admin_required
def ship_delete_handler(ship_id: int):   
    delete_ship(ship_id)
    return redirect('/admin/ship')


@admin_blueprint.route('/admin/reports', methods=['GET', 'POST'])
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


@admin_blueprint.route('/no_admin', methods=['GET', 'POST'])
def no_admin_handler():
    return render_template('no_admin.html')
   