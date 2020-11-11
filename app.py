import connexion
import logging
import connexion
from send_mail import init_email
from flask import request
from utils.dispaccer_events import DispatcherMessage
from app_constant import REGISTRATION_EMAIL


def confirm_registration():
    """
    This method is a flask method that send the confirm registration email
    to the user.
    """
    email_user = request.get_json("email")
    logging.debug("Email of new user: {}".format(email_user))
    name_user = request.get_json("name")
    logging.debug("Name new user: {}".format(name_user))
    DispatcherMessage.send_message(REGISTRATION_EMAIL, [email_user, name_user])
    return {"result": "OK"}, 200


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api("swagger.yml")
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


def init_flask_app(app):
    """
    This method init all the configuration from the flask app
    """
    app.config.from_object("config.DebugConfiguration")


if __name__ == "__main__":
    init_flask_app(application)
    app.run(port=5001)
