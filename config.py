import os

db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='notesapp')
db_user = os.environ.get('DB_USER', default='user')
db_pass = os.environ.get('DB_PASS', default='')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"