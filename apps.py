from users.main import app as users_app
from groups.main import app as groups_app

APPS = [
    ('/users', users_app),
    ('/groups', groups_app)
]
