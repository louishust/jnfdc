#!/usr/bin/env python
import os
import time

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def fetch_data():
    """Fetch jnfdc data"""
    from app.util.fetch import fetch_jnfdc
    while True:
        now = time.localtime()
        if now.tm_hour >= 8 and now.tm_hour <= 22:
            fetch_jnfdc()
        time.sleep(60)

@manager.command
def init_db():
    """Init Database"""
    from app.models import NetSign
    db.create_all()

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade
    # migrate database to latest revision
    upgrade()

if __name__ == '__main__':
    manager.run()
