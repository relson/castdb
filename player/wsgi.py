import sys
activate_this = "/var/www/__apppath__/env/bin/activate_this.py"

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

PROJECT_DIR = "/var/www/__apppath__/"

sys.path.insert(0, PROJECT_DIR)

from fplayer import app as application
