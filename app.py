from datetime import datetime

import connexion
import logging
import connexion
from flask import request, current_app
from utils.dispaccer_events import DispatcherMessage
from app_constant import REGISTRATION_EMAIL, CONFIRMATION_BOOKING


def confirm_registration():
    """
    This method is a flask method that send the confirm registration email
    to the user.
    """
    json = request.get_json()
    email_user = json["email"]
    current_app.logger.debug("Email of new user: {}".format(email_user))
    name_user = json["name"]
    current_app.logger.debug("Name new user: {}".format(name_user))
    DispatcherMessage.send_message(REGISTRATION_EMAIL, [email_user, name_user])
    return {"result": "OK"}, 200


def confirm_booking_registration():
    """
    This method send the email to confirm the booking
    """
    json = request.get_json()
    email_user = json["email_user"]
    current_app.logger.debug("User name: {}".format(email_user))
    user_name = json["user_name"]
    current_app.logger.debug("User name: {}".format(user_name))
    restaurant_name = json["restaurant_name"]
    current_app.logger.debug("Restaurant name: {}".format(restaurant_name))
    friends = json["friends"]
    current_app.logger.debug("Fiends: {}".format(friends))
    date_string = json["booking_time"]
    current_app.logger.debug("In date string: {}".format(date_string))
    booking_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    current_app.logger.debug("In date: {}".format(booking_time))
    DispatcherMessage.send_message(
        CONFIRMATION_BOOKING, [email_user, user_name, restaurant_name, friends, booking_time]
    )
    return {"result": "OK"}, 200


logging.basicConfig(level=logging.DEBUG)
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
