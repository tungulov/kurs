from flask import Blueprint, request, render_template
from src.connection import DBConnection, db_config, provider

ships_blueprint = Blueprint(
    'ships_bp',
    __name__,
    template_folder='templates'
)

@ships_blueprint.route('/ships', methods=['GET', 'POST'])
def ships():
    if request.method == 'POST':
        ship_tonnage = request.form['ship_tonnage']
        sql_statement = provider.get(
            'find_ship_by_tonnage.sql',
            {'ship_tonnage': ship_tonnage}
        )
        render_data = find_ship_by_tonnage(db_config, sql_statement)
        return render_template('list.html', render_data=render_data)

    return render_template('name_form.html')


def find_ship_by_tonnage(db_config, sql):
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        return {
            'status': True if result else False,
            'data': result
        }