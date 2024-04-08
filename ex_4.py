class User:
    """
    Class representing a user entity.

    Attributes:
        id (int): The unique identifier of the user.
        nick_name (str): The nickname of the user.
        first_name (str): The first name of the user.
        last_name (str, optional): The last name of the user.
        middle_name (str, optional): The middle name of the user.
        gender (str, optional): The gender of the user.
    """

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        Initializes a User instance with the provided information.

        Args:
            id (int): The unique identifier of the user.
            nick_name (str): The nickname of the user.
            first_name (str): The first name of the user.
            last_name (str, optional): The last name of the user.
            middle_name (str, optional): The middle name of the user.
            gender (str, optional): The gender of the user.
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, nick_name, last_name=None):
        """
        Updates the user's nickname and last name if provided.

        Args:
            nick_name (str): The new nickname to update.
            last_name (str, optional): The new last name to update.
        """
        if nick_name:
            self.nick_name = nick_name
        if last_name:
            self.last_name = last_name
    
    def __str__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: A formatted string containing user information.
        """
        return f'User: id = {self.id}, nick_name = {self.nick_name}, first_name = {self.first_name}, last_name = {self.last_name}, middle_name = {self.middle_name}, gender = {self.gender}'

