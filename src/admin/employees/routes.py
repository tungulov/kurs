from flask import Blueprint, request, render_template, session, redirect

from src.access import admin_required
from src.modules.employees_module import add_employee, delete_employee, edit_employee, get_employee, get_employees
from src.common.table_naming import employee_labels, employee_types

admin_employees_blueprint = Blueprint(
    'admin_employees_bp',
    __name__,
    template_folder='templates',
    url_prefix='/employee'
)

@admin_employees_blueprint.route('/', methods=['GET'])
@admin_required
def employee_handler():
    employees = get_employees()
    return render_template('employees.html', employees=employees, employee_labels=employee_labels)


@admin_employees_blueprint.route('/add', methods=['GET', 'POST'])
@admin_required
def employee_adding_handler():
    if request.method == 'POST':
        fio = request.form.get('fio', '')
        name = request.form.get('name', '')
        password = request.form.get('password', '')
        employee_type = request.form.get('employee_type', '')

        add_employee(fio, name, password, employee_type)
        return redirect('/admin/employee')
           
    return render_template('employee_edit.html', employee_types=employee_types, employee=None)


@admin_employees_blueprint.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
@admin_required
def ship_edit_handler(employee_id: int):
    if request.method == 'POST':
        fio = request.form.get('fio', '')
        name = request.form.get('name', '')
        password = request.form.get('password', '')
        employee_type = request.form.get('employee_type', '')
        restore_employee = request.form.get('restore_employee', 'off')
        
        edit_employee(employee_id, fio, name, password, employee_type, restore_employee)
        return redirect('/admin/employee')
    
    employee = get_employee(employee_id)
    return render_template('employee_edit.html', employee_types=employee_types, employee=employee)


@admin_employees_blueprint.route('/delete/<int:employee_id>', methods=['GET'])
@admin_required
def employee_delete_handler(employee_id: int):   
    delete_employee(employee_id)
    return redirect('/admin/employee')

