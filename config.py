from tempfile import gettempdir

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# configure session to use filesystem (instead of signed cookies)
SESSION_FILE_DIR = gettempdir()
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
PROPAGATE_EXCEPTIONS = True

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/Classroom"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
