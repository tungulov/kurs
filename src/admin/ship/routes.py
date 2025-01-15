from flask import Blueprint, request, render_template, session, redirect

from src.access import admin_required
from src.modules.ship_module import add_ship, delete_ship, edit_ship, get_ship, get_ships_types, get_ships
from src.common.table_naming import ship_labels

admin_ships_blueprint = Blueprint(
    'admin_ships_bp',
    __name__,
    template_folder='templates',
    url_prefix='/ship'
)


@admin_ships_blueprint.route('/', methods=['GET'])
@admin_required
def ship_handler():
    ships = get_ships()
    return render_template('ships.html', ships=ships, ship_labels=ship_labels)


@admin_ships_blueprint.route('/add', methods=['GET', 'POST'])
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


@admin_ships_blueprint.route('/edit/<int:ship_id>', methods=['GET', 'POST'])
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


@admin_ships_blueprint.route('/delete/<int:ship_id>', methods=['GET'])
@admin_required
def ship_delete_handler(ship_id: int):   
    delete_ship(ship_id)
    return redirect('/admin/ship')
