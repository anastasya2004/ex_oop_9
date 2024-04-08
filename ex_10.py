class Point:
    def __init__(self, coordinat=(0, 0)):
        """
        Initialize an instance of the Point class.
        
        Initializes a point with coordinates.
        
        Parameters:
            coordinates (tuple): A tuple containing x and y coordinates of the point.
        """
        self.x = coordinat[0]
        self.y = coordinat[1]
    

class Segment:
    def __init__(self, point1, point2):
        """
        Initialize an instance of the Segment class.
        
        Initializes a segment with two points.
        
        Parameters:
            point1 (Point): The starting point of the segment.
            point2 (Point): The ending point of the segment.
        """
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = False

    def __str__(self):
        """
        Returns a string representation of the segment.
        
        Parameters:
            None
        
        Returns:
            str: A string representation of the segment in the form "(point1, point2)".
        """
        return f'({self.point1}, {self.point2})'


class CoordinateSystem:
    def __init__(self):
        """
        Initialize an instance of the CoordinateSystem class.
        
        Initializes an empty list to store segments.
        
        Parameters:
            None
        """
        self.segments = []

    def add_segment(self, segment):
        """
        Adds a segment to the list of segments.
        
        Parameters:
            segment (Segment): The segment to be added.
        """
        self.segments.append(segment)

    def axis_intersection(self):
        """
        Finds the count of segments intersecting the axis.
        
        Parameters:
            None
        
        Returns:
            int: The count of segments intersecting the axis.
        """
        count = 0
        for segment in self.segments:
            if (segment.point1.x * segment.point2.x < 0 <= segment.point1.y * segment.point2.y) or (segment.point1.x * segment.point2.x >= 0 > segment.point1.y * segment.point2.y):
                count += 1
                segment.one_intersection = True
            else:
                segment.one_intersection = False
        return count
    
    def __str__(self):
        """
        Returns a string representation of the coordinate system.
        
        Parameters:
            None
        
        Returns:
            str: A string representation of the coordinate system containing all segments.
        """
        return ' '.join(str(elem) for elem in CoordinateSystem.segments)
