import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:littlebo@localhost/cicd-test'
SQLALCHEMY_DATABASE_URI = 'postgresql://wnxiezqnurlzma:2a0cb9582d0e2b35745b2329eb8b43f9c9640a35e808c7259f0d1f209f61b8bd@ec2-44-209-158-64.compute-1.amazonaws.com:5432/dc82cgq9gcqga0'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
