class NotSleeping:
    """
    Class representing a sleepless entity.

    Attributes:
        sheep_count (int): The count of sheep the entity has seen.
    """

    def __init__(self, sheep_count):
        """
        Initializes an instance of the NotSleeping class.

        Args:
            sheep_count (int): The initial count of sheep seen.
        """
        self.sheep_count = 0

    def add_sleep(self, count):
        """
        Adds the specified number of sheep to the count.

        Args:
            count (int): The number of sheep to add.
        """
        for i in range(count):
            self.sheep_count += 1
