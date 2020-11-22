from datetime import datetime


class RestaurantsModel:

    def fill_from_json(self, json_obj) -> None:
        """
        This method contains the logint to bing a json object with the model
        in this case the user
        :param json_obj: A object that looks like:
        {
            "name": "Il Ristorante che non c'è",
            "owner_email": "user@mail.com",
            "date_booking": {}
        }
        """
        self.name = json_obj["name"]
        self.owner_email = json_obj["email"]
        self.date_booking = datetime.strptime(json_obj["date_booking"], "%Y-%m-%dT%H:%M:%SZ")
        self.owner_name = json_obj["owner_name"]
        self.friends = json_obj["friends"]