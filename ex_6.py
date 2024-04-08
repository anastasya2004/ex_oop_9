class Point:
    """
    Represents a point with x and y coordinates.

    Attributes:
    - x: an integer representing the x-coordinate of the point.
    - y: an integer representing the y-coordinate of the point.

    Methods:
    - __init__: initializes a Point object with optional coordinates, default is (0, 0).
    - get_x: returns the x-coordinate of the point.
    - get_y: returns the y-coordinate of the point.
    - distance: calculates the Euclidean distance between two points.
    - sum: sums the coordinates of two points and returns a new point.
    - __str__: returns a string representation of the point.
    """
    def __init__(self, coordinat=(0, 0)):
        self.x = coordinat[0]
        self.y = coordinat[1]

    def get_x(self):
        """
        Returns the x-coordinate of the point.
        """
        return self.x
    
    def get_y(self):
        """
        Returns the y-coordinate of the point.
        """
        return self.y
    
    def distance(self, other):
        """
        Calculates the Euclidean distance between two points.

        Parameters:
        - other: another Point object to calculate the distance to.

        Returns:
        A float representing the Euclidean distance between two points.
        """
        dist_x = self.x - other.get_x()
        dist_y = self.y - other.get_y()
        return (dist_x**2 + dist_y**2)**0.5
    
    def sum(self, other):
        """
        Sums the coordinates of two points and returns a new point.

        Parameters:
        - other: another Point object to sum coordinates with.

        Returns:
        A tuple representing the coordinates of the new Point object.
        """
        new_x = self.x + other.get_x()
        new_y = self.y + other.get_y()
        return (new_x, new_y)
    
    def __str__(self):
        """
        Returns a string representation of the point.
        """
        return f'Point ({self.x}, {self.y})'

    

point_1 = Point((10, -5))
print(point_1)
print(point_1.get_x())
print(point_1.get_y())
point_2 = Point()
print(point_2)
point_3 = Point((5, -4))
print(point_3)
print(point_1.distance(point_3))
print(point_3.sum(point_1))


