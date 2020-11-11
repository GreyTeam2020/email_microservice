from os.path import abspath, dirname

_cwd = dirname(abspath(__file__))


class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "flask-session-insecure-secret-key"
    HASH_ROUNDS = 100000
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = "465"
    MAIL_USERNAME = "greyteam2020@gmail.com"
    MAIL_PASSWORD = "SJzStSXX8XBHvDjY"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class DebugConfiguration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "DEBUG_flask-session-insecure-secret-key"
    HASH_ROUNDS = 100000
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = "465"
    MAIL_USERNAME = "greyteam2020@gmail.com"
    MAIL_PASSWORD = "SJzStSXX8XBHvDjY"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
