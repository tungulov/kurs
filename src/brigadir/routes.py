from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.access import admin_required, brigadir_required
from src.modules.admin_module import call_procedure


brigadir_blueprint = Blueprint(
    'brigadir_bp',
    __name__,
    template_folder='templates'
)


@brigadir_blueprint.route('/brigadir', methods=['GET', 'POST'])
@brigadir_required
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


@brigadir_blueprint.route('/no_brigadir', methods=['GET'])
def no_brigadir_handler():
    return render_template('no_brigadir.html')
   