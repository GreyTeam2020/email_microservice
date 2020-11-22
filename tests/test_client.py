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
            "booking_time": "2017-07-21T17:32:28+00:00",
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
            "user_positive": {"email": "user@asu.edu", "name": "User"},
            "past_restaurants": [
                {
                    "name": "Il Ristorante che non c'è",
                    "owner_email": "user@mail.com",
                    "owner_name": "Owner",
                    "date_booking": "2017-07-21T17:32:28+00:00",
                    "friends": ["friend@email.com"],
                }
            ],
            "future_restaurants": [
                {
                    "name": "Il Ristorante che non c'è",
                    "owner_email": "user@mail.com",
                    "owner_name": "Owner",
                    "date_booking": "2017-07-21T17:32:28+00:00",
                    "friends": ["friend@email.com"],
                }
            ],
        }
        response = Utils.possible_covid_contact(client, request)
        assert response.status_code == 200
