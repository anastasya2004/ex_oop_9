class TrafficLight:
    """
    Represents a traffic light with three possible signals: 'зеленый', 'желтый', 'красный'.
    """

    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self):
        """
        Initializes a TrafficLight object with the current signal set to 'зеленый' and counter set to 0.
        """
        self.current_signal = 'зеленый'
        self.counter = 0

    def next_signal(self):
        """
        Updates the current signal of the traffic light based on the counter value.
        If the counter reaches 3, the signal changes to 'желтый'.
        """
        self.counter += 1
        if self.counter == 3:
            self.counter = -1
            self.current_signal = 'желтый'
        else:
            self.current_signal = TrafficLight.permissible_values[self.counter]


light_name = TrafficLight()
print(light_name.current_signal)
for _ in range(10):
    light_name.next_signal()
    print(light_name.current_signal)