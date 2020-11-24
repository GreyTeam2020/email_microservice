from datetime import datetime

from tests.utils_tests import Utils


class TestClient:
    def test_send_email_reg_confirmation(self, client):
        """
        This test perform the request inside the flask client to send
        the email
        :param client: flask test client
        """
        request = {"name": "Eleonora", "email": "ele@gmail.com"}
        response = Utils.new_registration(client, request)
        assert response.status_code == 200

    def test_send_email_book_confirmation(self, client):
        """
        This test perform the request inside the flask client to send
        the email
        :param client: flask test client
        """
        request = {
            "email_user": "amazing@email.com",
            "user_name": "Giorgia",
            "restaurant_name": "Il Pomodorino",
            "friends": ["friend@email.com"],
            "booking_time": "2017-07-21T17:32:28Z",
        }
        response = Utils.new_booking(client, request)
        assert response.status_code == 200

    def test_send_email_posible_covid_contact(self, client):
        """
        This test perform the request inside the flask client to send
        the email
        :param client: flask test client
        """
        request = {
                "friends": ["a@s.me"],
                "contacts": [
                    {
                    "email": "a@a.com",
                    "name": "user.firstname",
                    "restaurant_name": "restaurant.name",
                    "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    }],
                "past_restaurants": [
                    {
                    "email": "a@a.com",
                    "name": "restaurant.name",
                    "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    }],
                "reservation_restaurants": [
                    {
                        "email": "v@a.com",
                        "name": "restaurant.name",
                        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "customer_email": "customer_email@email.com",
                    }
                ],
        }
        response = Utils.possible_covid_contact(client, request)
        assert response.status_code == 200
