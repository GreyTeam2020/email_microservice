from celery import Celery
from flask import Flask

from send_mail import (
    send_registration_confirm,
    send_possible_positive_contact_to_friend,
    send_possible_positive_contact,
    send_booking_confirmation_to_friends,
    send_positive_in_restaurant,
    send_positive_booking_in_restaurant,
    init_email
)

_CELERY = True


def create_celery_app():
    """
    This application create the flask app for the worker
    Thanks https://github.com/nebularazer/flask-celery-example
    """
    ## redis inside the http is the name of network that is called like the containser
    BACKEND = "redis://{}:{}".format("rd01", "6379")
    BROKER = "redis://{}:{}/0".format("rd01", "6379")
    if _CELERY is True:
        return Celery(__name__, backend=BACKEND, broker=BROKER)
    app = Flask(__name__)
    app.config.from_object("config.DebugConfiguration")

    celery_app = Celery(app.import_name, backend=BACKEND, broker=BROKER)

    init_email(app)
    # celery.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask

    return celery_app


celery_app = create_celery_app()


@celery_app.task()
def send_email_to_confirm_registration(to_email: str, to_name: str, with_toke: str):
    """
    Perform the celery task to send the email registration
    it take the following element
    :param to_email: Email to send the message
    :param to_name: The user name to send the message
    :param with_toke: The token of user on system
    """
    send_registration_confirm(to_email, to_name, with_toke)


@celery_app.task()
def send_alert_new_covid19_about_previous_booking(
    to_email: str, to_name: str, email_user: str, restaurant_name: str
):
    """
    Perform the send email with celery async task to send a email to all restaurants with a booking from the person
    positive to covid19.
    :param to_email:
    :param to_name:
    :param email_user:
    :param restaurant_name:
    :return:
    """
    send_positive_booking_in_restaurant(to_email, to_name, email_user, restaurant_name)


@celery_app.task()
def send_positive_in_restaurant_celery(
    to_email: str, to_name: str, date_possible_contact: str, restaurant_name: str
):
    """
    Perform the send email with celery async task to send an email to the restaurant where a new positive cases was
    """
    send_positive_in_restaurant(
        to_email, to_name, date_possible_contact, restaurant_name
    )


@celery_app.task()
def send_possible_positive_contact_to_friend_celery(
    to_email: str, date_possible_contact: str, restaurant_name: str
):
    """
    Perform the send email with celery async task to send an email to friends with a reservation
    :param to_email:
    :param date_possible_contact:
    :param restaurant_name:
    """
    send_possible_positive_contact_to_friend(
        to_email, date_possible_contact, restaurant_name
    )


@celery_app.task()
def send_possible_positive_contact_celery(
    to_email: str, to_name: str, date_possible_contact: str, restaurant_name: str
):
    """
    Perform the send email with celery async task to send an email to the customer in a restaurants where a new positive
    case was
    :param to_email:
    :param to_name:
    :param date_possible_contact:
    :param restaurant_name:
    """
    send_possible_positive_contact(
        to_email, to_name, date_possible_contact, restaurant_name
    )


@celery_app.task()
def send_booking_confirmation_to_friends_celery(
    to_email: str, to_name: str, to_restaurants: str, to_friend_list: [], date_time
):
    """

    :param to_email:
    :param to_name:
    :param to_restaurants:
    :param to_friend_list:
    :param date_time:
    :return:
    """
    send_booking_confirmation_to_friends(
        to_email, to_name, to_restaurants, to_friend_list, date_time
    )
