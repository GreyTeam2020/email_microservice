from datetime import datetime

import connexion
import logging
import connexion
from flask import request, current_app
from utils.dispaccer_events import DispatcherMessage
from app_constant import (
    REGISTRATION_EMAIL,
    CONFIRMATION_BOOKING,
    NEW_POSITIVE_WAS_IN_RESTAURANT,
    EMAIL_TO_FRIEND,
    NEW_COVID_TO_RESTAURANT_BOOKING,
)
from model.past_restaurant_model import PastRestaurantsModel
from model.future_restaurant_model import FutureRestaurantsModel
from model.user_model import UserModel


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
        CONFIRMATION_BOOKING,
        [email_user, user_name, restaurant_name, friends, booking_time],
    )
    return {"result": "OK"}, 200


def send_possible_covid_contact():
    """
    This is the unique method to send the possible covid19 contacts email.
    :return: the flask response that looks like {"result": "OK"} with status code 200

    {
            "friends": ["a@s.me],
            "contacts": [{
                                    "email": user.email,
                                    "name": user.firstname,
                                    "restaurant_name": restaurant.name,
                                    "date": start,
                                }],
            "past_restaurants": [{
                            "email": restaurant["owner_email"],
                            "name": restaurant["name"],
                            "date": start,
                        }],
            "reservation_restaurants": [{
                        "email": restaurant["owner_email"],
                        "name": restaurant["name"],
                        "date": date,
                        "customer_email": customer_email,
                    }],
        }
    """
    json_request = request.get_json()
    current_app.logger.debug("Request with body\n{}".format(json_request))

    json_friends = json_request["friends"]
    current_app.logger.debug("List of friend is: {}".format(json_friends))
    for json_friend in json_friends:
        DispatcherMessage.send_message(
            EMAIL_TO_FRIEND,
            [
                json_friend,
                "",
                "",
            ],
        )

    # A message to the friends, it take the following paramiters
    # to_email, date_possible_contact, restaurant_name
    json_users = json_request["contacts"]
    contacts = []
    for json_user in json_users:
        user_positive = UserModel()
        user_positive.fill_from_json(json_user)
        contacts.append(user_positive)

    # A message to the restaurants booking
    # to_email, to_name, email_user, restaurant_name
    json_restaurant = json_request["past_restaurants"]
    restaurants = []
    for json_rest in json_restaurant:
        restaurant = PastRestaurantsModel()
        restaurant.fill_from_json(json_rest)
        restaurants.append(restaurant)
        DispatcherMessage.send_message(
            NEW_POSITIVE_WAS_IN_RESTAURANT,
            [
                restaurant.owner_email,
                restaurant.owner_email,
                str(restaurant.date_booking),
                restaurant.name,
            ],
        )

    json_restaurant = json_request["reservation_restaurants"]
    restaurants = []
    for json_rest in json_restaurant:
        restaurant = FutureRestaurantsModel()
        restaurant.fill_from_json(json_rest)
        restaurants.append(restaurant)
        DispatcherMessage.send_message(
            NEW_COVID_TO_RESTAURANT_BOOKING,
            [
                restaurant.owner_email,
                restaurant.owner_email,
                str(restaurant.date_booking),
                restaurant.name,
            ],
        )

    return {"result": "OK"}, 200


logging.basicConfig(level=logging.DEBUG)
app = connexion.App(__name__)
app.add_api("swagger.yml")
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


def init_flask_app(app, conf_type: str = "config.DebugConfiguration"):
    """
    This method init all the configuration from the flask app
    """
    app.config.from_object(conf_type)


if __name__ == "__main__":
    # init_flask_app(application)
    init_flask_app(application, "config.BaseConfiguration")
    app.run(port=5001)
