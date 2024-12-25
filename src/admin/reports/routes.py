from flask import Blueprint, request, render_template, session, redirect
from src.connection import DBConnection, db_config, provider
from src.access import admin_required


from src.modules.reports_module import employee_statistic, task_statistic, ship_statistic

admin_reports_blueprint = Blueprint(
    'record_bp',
    __name__,
    template_folder='templates',
    url_prefix='/reports'
)

@admin_reports_blueprint.route('/', methods=['GET'])
@admin_required
def reports():
    return render_template('reports.html')


@admin_reports_blueprint.route('/employees_statistic', methods=['GET', 'POST'])
@admin_required
def employees_statistic_handler():
    month = request.form.get('month', None)
    year = request.form.get('year', None)

    statistic = None
    if month and year:
        statistic = employee_statistic(month, year)

    return render_template('employees_statistic.html', statistic=statistic)


@admin_reports_blueprint.route('/task_statistic', methods=['GET', 'POST'])
@admin_required
def task_statistic_handler():
    month = request.form.get('month', None)
    year = request.form.get('year', None)

    statistic = None
    if month and year:
        statistic = task_statistic(month, year)
    
    return render_template('brigade_statistic.html', statistic=statistic)


@admin_reports_blueprint.route('/ship_statistic', methods=['GET', 'POST'])
@admin_required
def ship_statistic_handler():
    month = request.form.get('month', None)
    year = request.form.get('year', None)

    statistic = None
    if month and year:
        statistic = ship_statistic(month, year)
    
    return render_template('ship_statistic.html', statistic=statistic)

