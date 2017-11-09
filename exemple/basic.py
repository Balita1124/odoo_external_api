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


#-------------------------------------------------------
# Reading data from server
#-------------------------------------------------------

api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)

try:
    nb = api.execute_kw(db, uid, ui_pwd, 'res.partner', 'search_count', [[('parent_id', '!=', False)]])
    print "nombre de contact parent " + str(nb)
except Exception as e:
    print e


# ----------------------------------------------------------
# Calling other method
# ----------------------------------------------------------

"""
 The remaining model methods are all exposed through RPC, except for those starting
    with "_" that are conidered private.
"""

# create
api.execute_kw(db, uid, ui_pwd, 'res.partner', 'create', [{'name':'Packt'}])
# write
api.execute_kw(db, uid, ui_pwd, 'res.partner', 'write', [[75],{'name': 'Packt Pub'}])
# read
api.execute_kw(db, uid, ui_pwd, 'res.partner', 'read', [[75], ['id','name']])
# delete
api.execute_kw(db, uid, ui_pwd, 'res.partner', 'unlink', [[75]])


# ------------------------------------------------------------
# Inspection
# ------------------------------------------------------------

api.execute_kw(    db, uid, ui_pwd, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})


