class Game:
    """
    Class representing a game between two teams.

    Attributes:
        command1_name (str): The name of the first team.
        command2_name (str): The name of the second team.
        command1_score (int): The score of the first team.
        command2_score (int): The score of the second team.
    """

    def __init__(self, kwarg):
        """
        Initializes a Game instance with the provided team names.

        Args:
            kwarg (dict): A dictionary containing 'command1' and 'command2' keys with team names.
        """
        self.command1_name = kwarg['command1']
        self.command2_name = kwarg['command2']
        self.command1_score = 0
        self.command2_score = 0

    def ball_thrown(self, command, point):
        """
        Updates the score of the corresponding team based on the command and points.

        Args:
            command (int): The team number (1 or 2).
            point (int): The points scored.
        """
        if command == 1:
            self.command1_score += point
        if command == 2:
            self.command2_score += point

    def get_score(self):
        """
        Returns the current scores of both teams.

        Returns:
            tuple: A tuple containing the scores of the first and second teams.
        """
        return self.command1_score, self.command2_score

    def get_winner(self):
        """
        Determines and returns the winner of the game based on the scores.

        Returns:
            str: The name of the winning team or 'ничья' for a tie.
        """
        if self.command1_score > self.command2_score:
            return self.command1_name
        elif self.command1_score < self.command2_score:
            return self.command2_name
        else:
            return 'ничья'

    def __str__(self):
        """
        Returns a string representation of the Game instance.

        Returns:
            str: A formatted string containing team names and scores.
        """
        return (f'{self.command1_name}: {self.command1_score}, '
                f'{self.command2_name}: {self.command2_score}')


first_game = Game({'command1': 'Первые', 'command2': 'Вторые'})
first_game.ball_thrown(1, 2)
first_game.ball_thrown(1, 3)
first_game.ball_thrown(2, 3)
first_game.ball_thrown(2, 2)
first_game.ball_thrown(1, 2)
print(first_game.get_score())
print(first_game.get_winner())
print(first_game)