# import os

# SECRET_KEY = os.urandom(32)

# # Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

# # Enable debug mode.
# DEBUG = True

# # Connect to the database
# # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:littlebo@localhost/cicd-test'
# SQLALCHEMY_DATABASE_URI = 'postgresql://wnxiezqnurlzma:2a0cb9582d0e2b35745b2329eb8b43f9c9640a35e808c7259f0d1f209f61b8bd@ec2-44-209-158-64.compute-1.amazonaws.com:5432/dc82cgq9gcqga0'

# # Turn off the Flask-SQLAlchemy event system and warning
# SQLALCHEMY_TRACK_MODIFICATIONS = False







class Config(object):
    DEBUG = False
    TESTING = False


class LocalConfig(Config):
    DB_USER_NAME = 'postgres'
    DB_USER_PWD = 'littlebo'
    DB_HOST = 'localhost'
    DB_NAME = 'cicd-test'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
        username=DB_USER_NAME,
        password=DB_USER_PWD,
        host=DB_HOST,
        db=DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class GithubActionsConfig(Config):
    DB_USER_NAME = 'postgres'
    DB_USER_PWD = 'littlebo'
    DB_HOST = 'localhost'
    DB_NAME = 'cicd-test'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
        username=DB_USER_NAME,
        password=DB_USER_PWD,
        host=DB_HOST,
        db=DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DB_USER_NAME = 'wnxiezqnurlzma'
    DB_USER_PWD = '2a0cb9582d0e2b35745b2329eb8b43f9c9640a35e808c7259f0d1f209f61b8bd'
    DB_HOST = 'ec2-44-209-158-64.compute-1.amazonaws.com'
    DB_NAME = 'dc82cgq9gcqga0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
        username=DB_USER_NAME,
        password=DB_USER_PWD,
        host=DB_HOST,
        db=DB_NAME
    )


class StagingConfig(Config):
    # DB_USER_NAME = 'hkicrnmcexpigf'
    # DB_USER_PWD = '7b9bddbc26f8a27da397e3a2a62d172b9493d8b1186eb2ab845f2b2d9e8ecbce'
    # DB_HOST = 'ec2-44-205-63-142.compute-1.amazonaws.com'
    # DB_NAME = 'dde83isf1i43ur'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
    #     username=DB_USER_NAME,
    #     password=DB_USER_PWD,
    #     host=DB_HOST,
    #     db=DB_NAME
    # )
    DB_USER_NAME = 'gdkrkkddbtxoar'
    DB_USER_PWD = '5a8c3d89f9cf4df8c5d058cbe7d8e1633fa805960c49b2ba8cc17ecb3b26b8b3'
    DB_HOST = 'ec2-107-23-76-12.compute-1.amazonaws.com'
    DB_NAME = 'd52lbnuf2g1r3d'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
        username=DB_USER_NAME,
        password=DB_USER_PWD,
        host=DB_HOST,
        db=DB_NAME
    )


class ProductionConfig(Config):
    DB_USER_NAME = 'gdkrkkddbtxoar'
    DB_USER_PWD = '5a8c3d89f9cf4df8c5d058cbe7d8e1633fa805960c49b2ba8cc17ecb3b26b8b3'
    DB_HOST = 'ec2-107-23-76-12.compute-1.amazonaws.com'
    DB_NAME = 'd52lbnuf2g1r3d'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(
        username=DB_USER_NAME,
        password=DB_USER_PWD,
        host=DB_HOST,
        db=DB_NAME
    )
