# Python Anywhere Notes

# Creating Virtual Env on Python Anywhere:
# Input -> mkvirtualenv --python=python(most recent version) environmentname

# To check out installed pacakges -> pip list

# To install Django -> pip install -U django==(django version for project)

# All libraries used in project need to be isntalled in console

# Must clone repo to console

# Must run migrations first - python manage.py makemigrations app_name
# Then -> python manage.py migrate

# Create superuser in same fashion

# Setting Up WSGI settings:
# Under Web tab in dashboard, click add a new web app
# Then follow instructions

# If app already created, click manual configuration
# Then click webapp setup page
# Look for VirtualEnv and click on link
# /home/(username)/.virtualenvs/(nameOfVirtualEnv)

# Setting Up Source Code:
# In console for the project get directory of project
# Then paste it in source code on same page as manual config

# WSGI Config:
# Delete Hello World code
# Uncomment most django code
path = "/home/(username)/(repo_name)/(project_name)"
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODEUL", "(directory_name).settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Then click save

# Loading Static Files:
# Under Web Tab
# Static Files for Admin & Static Files for App

# For Admin:
# URL -> /static/admin
# Directory -> /home/(username)/.virtualenvs/(virtualEnvName)/lib/python(version)/site-packages/django/contrib/admin/static/admin

# Then reload Web App

# Turn off Debug mode:
# Under Files Tab:
# Navigate to settings.py
# settings.py file -> ALLOWED_HOSTS = ["(username).(hostname)"]
# DEBUG = False
# Then save

# Reload web app again

# For Static Files:
# URL -> /static
# Directory -> /home/(username)/(relative_path)