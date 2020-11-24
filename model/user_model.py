class UserModel:
    def fill_from_json(self, json_obj) -> None:
        """
        This method contains the logint to bing a json object with the model
        in this case the user
        :param json_obj: A object that looks like:
        {
                                    "email": user.email,
                                    "name": user.firstname,
                                    "restaurant_name": restaurant.name,
                                    "date": start,
                                }
        """
        self.name = json_obj["name"]
        self.email = json_obj["email"]
        self.restaurant_name = json_obj["restaurant_name"]
        self.date = json_obj["date"]
