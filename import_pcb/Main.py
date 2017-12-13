# -*- coding: utf-8 -*-

from base_import import BaseImport

columns = ['state', 'id', 'default_code', 'name_template', 'weight', 'weight_net', 'volume', 'x_pcb']
new_import = BaseImport()

data = new_import.import_file('file.xlsx', 'pour_import', columns)
print data
