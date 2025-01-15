from flask import Blueprint, request, render_template, session, redirect

from src.access import brigadir_required
from src.modules.brigadir_module import add_brigade, get_brigade_with_ship_and_workers, get_workers, get_all_brigades_with_ship_and_employees_count, set_brigade_data
from src.modules.ship_module import get_ships, get_unloaded_ships
from src.common.table_naming import employee_labels, brigades_labels


brigadir_blueprint = Blueprint(
    'brigadir_bp',
    __name__,
    template_folder='templates',
    url_prefix='/brigade'
)


@brigadir_blueprint.route('/new', methods=['GET', 'POST'])
@brigadir_required
def new_brigade_handler():
    if request.method == 'POST':
        date_created = request.form['date_created']
        ship_id = request.form.get('ship_id', None)
        ships = get_unloaded_ships(date_created)
        workers = get_workers(date_created)
        
        if ship_id:
            selected_employers = []
            for key in request.form:
                if 'employee_' in key:
                    selected_employers.append(int(key.split('_')[-1]))
            if len(selected_employers) == 0:
                return render_template('brigadir.html', error = 'Вы не выбрали ни одного работника', employees=workers, employee_labels=employee_labels, ships=ships, len_ships=len(ships))

            add_brigade(ship_id, selected_employers, date_created)
            return redirect('/')
        
        return render_template('brigadir.html', employees=workers, employee_labels=employee_labels, ships=ships, len_ships=len(ships))

    return render_template('brigadir.html')


@brigadir_blueprint.route('/info', methods=['GET', 'POST'])
@brigadir_required
def info_brigade_handler():
    brigades = get_all_brigades_with_ship_and_employees_count()
    return render_template('brigades_info.html', brigades=brigades, brigades_labels=brigades_labels)


@brigadir_blueprint.route('/about/<int:brigade_id>', methods=['GET', 'POST'])
@brigadir_required
def brigade_about_handler(brigade_id: int):
    employees = get_brigade_with_ship_and_workers(brigade_id)

    if request.method == 'POST':
        status = request.form.get('status')
        selected_brigade_employers = []
        for key in request.form:
            if 'hours_' in key:
                selected_brigade_employers.append([int(key.split('_')[-1]), request.form[key]])
        
        set_brigade_data(brigade_id, selected_brigade_employers, status)
        return redirect('/brigade/info')

    return render_template('brigades_about.html', brigades=employees)


@brigadir_blueprint.route('/no_brigadir', methods=['GET'])
def no_brigadir_handler():
    return render_template('no_brigadir.html')
   