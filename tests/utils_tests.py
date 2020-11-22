class Utils:
    """
    This class contains all logic to implement the client request
    to make a simple component test.
    """

    @staticmethod
    def new_registration(client, params):
        """
        This request perform the flask request to test if the method works with params
        :param client: flask test client
        :param params: the body that the request accept
        :return: the client response
        """
        return client.post("/send_email/confirm_registration", json=params)

    @staticmethod
    def new_booking(client, params):
        """
        This request perform the flask request to test if the method works with params
        :param client: flask test client
        :param params: the body that the request accept
        :return: the client response
        """
        return client.post("/send_email/booking_confirmation", json=params)

    @staticmethod
    def possible_covid_contact(client, params):
        """
        This request perform the flask request to test if the method works with params
        :param client: flask test client
        :param params: the body that the request accept
        :return: the client response
        """
        return client.post("/send_email/send_contact", json=params)
