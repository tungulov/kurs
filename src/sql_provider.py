import os
from string import Template


class SqlProvider:
    def __init__(self, path):
        self._scripts = {}
        for file in os.listdir(path):
            if file.endswith('.sql'):
                self._scripts[file] = Template(
                    open(f'{path}/{file}', 'r').read()
                )

    def get(self, name, params = None):
        if name not in self._scripts:
            raise ValueError(f'No such sql_template: {name}')
        if params:
            return self._scripts[name].substitute(**params)
        return self._scripts[name].substitute()