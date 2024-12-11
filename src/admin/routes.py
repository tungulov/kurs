from flask import Blueprint, request, render_template, session, redirect

from src.connection import DBConnection, db_config, provider
from src.access import admin_required


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


def call_procedure(db_config, sql):
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]

        return {
            'status': True if result else False,
            'ships': result
        }

@admin_blueprint.route('/no_admin', methods=['GET', 'POST'])
def no_admin_handler():
    return render_template('no_admin.html')
   