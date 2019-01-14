'''
For testing purposes
'''

from bvje import Role, User, app
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask_migrate import Migrate


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
# if session.commit() fails, delete the database and create a new one
db.session.commit()


# change db value
admin_role.name = "Administrator"
db.session.add(admin_role)
db.session.commit()



# query rows - wrapping the method calls in str() will return the SQL query
Role.query.all()
User.query.all()
User.query.filter_by(role=mem_role).all()


# support for db migrations - run 'flask db init' create migration script with 'flask db migrate'
# upgrade the db using 'flask db upgrade
migrate = Migrate(app, db)