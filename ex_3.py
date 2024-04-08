class NotSleeping:
    """
    Class representing a sleepless entity.

    Attributes:
        sheep_count (int): The count of sheep the entity has seen.
    """

    def __init__(self):
        """
        Initializes an instance of the NotSleeping class with a sheep count of 0.
        """
        self.sheep_count = 0

    def add_sleep(self, count):
        """
        Adds the specified number of sheep to the count.

        Args:
            count (int): The number of sheep to add.
        """
        self.sheep_count += count

    def lost(self, count):
        """
        Increments the sheep count by 1 for the specified number of times.

        Args:
            count (int): The number of times to increment the sheep count by 1.
        """
        for i in range(count):
            self.sheep_count += 1

    def get_count_sheeps(self):
        """
        Returns the current sheep count.

        Returns:
            int: The current count of sheep seen.
        """
        return self.sheep_count
