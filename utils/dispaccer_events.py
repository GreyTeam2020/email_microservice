from app_constant import *
from background import (
    send_email_to_confirm_registration,
    send_alert_new_covid19_about_previous_booking,
    send_possible_positive_contact_to_friend_celery,
    send_booking_confirmation_to_friends_celery,
    send_positive_in_restaurant_celery,
)

_CELERY = True


class DispatcherMessage:
    """
    This class using a mediator patter to decide if the status of app admit
    the celery message.
    The celery message are available for the moment only in release and in some debug cases
    otherwise it is disabled.

    For instance, for the testing it is disabled.

    @author Vincenzo Palazzo v.palazzo1@studenti.unipi.it
    """

    @staticmethod
    def send_message(type_message: str, params):
        """
        This static method take and string that usually is defined inside the
        file app_constant.py and check if there is condition to dispatc the test
        :return: nothings
        """
        if _CELERY is False:
            return
        if type_message == REGISTRATION_EMAIL: #V
            send_email_to_confirm_registration.apply_async(args=params)
        elif type_message == NEW_COVID_TO_RESTAURANT_BOOKING: #V
            send_alert_new_covid19_about_previous_booking.apply_async(args=params)
        elif type_message == NEW_POSITIVE_WAS_IN_RESTAURANT: #v
            send_positive_in_restaurant_celery.apply_async(args=params)
        elif type_message == EMAIL_TO_FRIEND: #V
            send_possible_positive_contact_to_friend_celery.apply_async(args=params)
        elif type_message == CONFIRMATION_BOOKING: #V
            send_booking_confirmation_to_friends_celery.apply_async(args=params)