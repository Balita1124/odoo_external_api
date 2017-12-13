# -*- coding: utf-8 -*-


from lxml import etree as ET
from petl import xlsx
import petl
import codecs
import string
import time
from datetime import datetime
import base64

class BaseImport:

    def import_file(self, filename, sheet, columns):
        """
        used to import file and return dictionnary of data
        :param filename:
        :param sheet:
        :param columns:
        :return data: dictionnary
        """
        table = xlsx.fromxlsx(filename, sheet)
        data = []
        for el in petl.records(table):
            data_child = {}
            for col in columns:
                data_child[col] = el[col]
            data.append(data_child)
        return data








