from flask import Blueprint, request, render_template, session, redirect
from src.connection import DBConnection, db_config, provider

from src.modules.reports_module import employee_statistic

admin_reports_blueprint = Blueprint(
    'record_bp',
    __name__,
    template_folder='templates',
    url_prefix='/reports'
)

@admin_reports_blueprint.route('/', methods=['GET'])
def reports():
    return render_template('reports.html')


@admin_reports_blueprint.route('/employees_statistic', methods=['GET', 'POST'])
def ships():
    month = request.form.get('month', None)
    year = request.form.get('year', None)

    statistic = None
    if month and year:
        statistic = employee_statistic(month, year)

    return render_template('employees_statistic.html', statistic=statistic)