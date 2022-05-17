# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "django-insecure-q5gi#6i1gen$85yaepkh+#ml(652!k8&^m3wt^d057wna8jo=9"
NEVERCACHE_KEY = "5_l-ld0gud-%_ds%wh36!l0q0rqsr1wh+ecdy26!pyvk)vs_1z"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "::1"]
