from datetime import datetime


class FutureRestaurantsModel:
    def fill_from_json(self, json_obj) -> None:
        """
        This method contains the logint to bing a json object with the model
        in this case the user
        :param json_obj: A object that looks like:
        "future_restaurants": {
                        "email": restaurant["owner_email"],
                        "name": restaurant["name"],
                        "date": date,
                        "customer_email": customer_email,
                    }
        """
        self.name = json_obj["name"]
        self.owner_email = json_obj["email"]
        self.date_booking = datetime.strptime(
            json_obj["date"], "%Y-%m-%dT%H:%M:%SZ"
        )
        self.customer_email = json_obj["customer_email"]
