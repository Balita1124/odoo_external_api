#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author : Rico Fauchard
# Year: 2017

# Communication xml-rpc

import xmlrpclib
srv, db = 'http://localhost:8090', 'socolait_v2.1.1_xml'
user, pwd = 'odoo10', 'odoo10'

ui_username,ui_pwd = 'admin', '123admin456'

#-------------------------------
# Printing server information
#--------------------------------

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % srv)

# ---------------------------------------------------
# Authentication
# ---------------------------------------------------

uid = common.authenticate(db, ui_username, ui_pwd, {})

if uid:

    api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)

    # create
    res_id = api.execute_kw(db, uid, ui_pwd, 'res.partner', 'create', [{
                            'name':'FRS10',
                            'supplier': True,
                            'customer': False,
                            'state':'validated',
                            'active' : True
    }])

    if res_id:
        ref = api.execute_kw(db, uid, ui_pwd, 'ir.model.data', 'create', [{
                            'module':'socolait_fournisseurs',
                            'name': 'frs00010',
                            'noupdate': True,
                            'model': 'res.partner',
                            'res_id': res_id,
        }])
    id = api.execute_kw(db, uid, ui_pwd, 'ir.model.data', 'get_object_reference', ['socolait_fournisseurs', 'frs00010'],{})

    print id[1]


else:
    print "auth failed"



