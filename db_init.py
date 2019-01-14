'''
For testing purposes
'''

from bvje import Role, User, app
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


db = SQLAlchemy(app)
db.create_all()
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
mem_role = Role(name='Member')
inact_role = Role(name='Inactive')
test_admin = User(username='testadmin', role=admin_role)
test_mod = User(username='testmod', role=admin_role)
test_mem = User(username='testmem', role=mem_role)
test_inact = User(username='testinact', role=inact_role)
db.session.add_all([admin_role, mod_role, mem_role, inact_role, test_admin, test_mem, test_mod, test_inact])
db.session.commit()