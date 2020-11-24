from .app_constant import *
from .send_mail import init_email
from .background import (
    send_email_to_confirm_registration,
    send_alert_new_covid19_about_previous_booking,
    send_possible_positive_contact_to_friend,
    send_booking_confirmation_to_friends_celery,
    send_positive_in_restaurant,
    celery_app,
)
