import xmlrpclib
srv, db = 'http://localhost:8090', 'socolait_v2.2.0_vierge'
user, pwd = 'odoo10', 'odoo10'

ui_username, ui_pwd = 'admin', '123admin456'

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
    spos = api.execute_kw(db, uid, ui_pwd, 'stock.pack.operation', 'search', [[]])

    for val in spos:
        spo = api.execute_kw(db, uid, ui_pwd, 'stock.pack.operation', 'read', [val])
        api.execute_kw(db, uid, ui_pwd, 'stock.pack.operation', 'write', [[val], {'product_qty': spo[0]['product_qty']}])



