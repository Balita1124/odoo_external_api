# Communication xml-rpc


import xmlrpclib
srv, db = 'http://localhost:8090', 'socolait_v2.1.1'
user, pwd = 'odoo10', 'odoo10'

ui_username,ui_pwd = 'admin', '123admin456'

#-------------------------------
# Printing server information
#--------------------------------

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % srv)
print common.version()

# ---------------------------------------------------
# Authentication
# ---------------------------------------------------

uid = common.authenticate(db, ui_username, ui_pwd, {})

if uid:
    print "succesful auth"
else:
    print "auth faild"

api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)
fields_get = api.execute_kw(db, uid, ui_pwd, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

print fields_get


