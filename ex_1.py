class Dog:
    """
    Class representing a dog.

    Attributes:
        name (str): The name of the dog.
    """

    def __init__(self, name):
        """
        Initializes an instance of the Dog class.

        Args:
            name (str): The name of the dog.
        """
        self.name = name

    def say(self):
        """
        Function to make the dog sound.

        Returns:
            str: A string representing the sound the dog makes.
        """
        return f'{self.name}: gav'
