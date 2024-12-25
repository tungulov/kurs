from flask import Blueprint, request, render_template, session, redirect

from src.access import brigadir_required
from src.modules.brigadir_module import add_brigade, get_workers, get_all_brigades_with_ship_and_employees_count
from src.modules.ship_module import get_ships
from src.common.table_naming import employee_labels


brigadir_blueprint = Blueprint(
    'brigadir_bp',
    __name__,
    template_folder='templates',
    url_prefix='/brigade'
)


@brigadir_blueprint.route('/new', methods=['GET', 'POST'])
@brigadir_required
def new_brigade_handler():
    ships = get_ships()
    workers = get_workers()

    if request.method == 'POST':
        selected_employers = []
        for key in request.form:
            if 'employee_' in key:
                selected_employers.append(int(key.split('_')[-1]))
        ship_id = request.form.get('ship_id', -1)
        if len(selected_employers) == 0:
            return render_template('brigadir.html', error = 'Вы не выбрали ни одного работника', employees=workers, employee_labels=employee_labels, ships=ships)

        add_brigade(ship_id, selected_employers)
        return redirect('/')

    return render_template('brigadir.html', employees=workers, employee_labels=employee_labels, ships=ships)


@brigadir_blueprint.route('/info', methods=['GET', 'POST'])
@brigadir_required
def info_brigade_handler():
    brigades = get_all_brigades_with_ship_and_employees_count()
    print(brigades)
    return render_template('brigadir.html', employees=brigades, employee_labels=employee_labels)


@brigadir_blueprint.route('/no_brigadir', methods=['GET'])
def no_brigadir_handler():
    return render_template('no_brigadir.html')
   