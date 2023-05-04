from src.vector_3d import Vector3D


class Line3D:
    """
    Represents a line in three dimensions. Uses a position vector p and direction vector d to define the line.

    Represents the following parametric equations:
    x = a * t + x0
    y = b * t + y0
    z = c * t + z0

    Notes:
        - Implements as many operations as possible with efficient numpy functions.

    Attributes:
        position (Vector3D): Represents the position vector for this line.
        direction (Vector3D): Represents the direction vector for this line.
        a (float): Represents the x coefficient in the parametric equation.
        b (float): Represents the y coefficient in the parametric equation.
        c (float): Represents the z coefficient in the parametric equation.
        x0 (float): Represents the x constant in the parametric equation.
        y0 (float): Represents the x constant in the parametric equation.
        z0 (float): Represents the x constant in the parametric equation.
    """

    def __init__(self, position, direction):
        """
        Initializes a new Line3D from a position vector and direction vector. 
        Normalizes the direction vector, then calculates a, b, c, x0, y0, and z0 from p and d.

        Parameters:
            position (Vector3D): The position vector for this line
            direction (Vector3D): The direction vector for this line
        """
        self.position = position
        self.direction = direction
        self.a = direction.x
        self.b = direction.y
        self.c = direction.z
        self.x0 = position.x
        self.y0 = position.y
        self.z0 = position.z

    @classmethod
    def from_two_points(cls, a, b):
        """
        Initializes a Line3D going from point a to point b.

        Makes the position vector a and the direction vector b - a.

        Args:
            a (Vector3D): The position vector for the first point.
            b (Vector3D): The position vector for the second point.
        """
        return cls(a, b - a)

    def __repr__(self):
        """
        Converts this Line3D into a human-readable representation

        Returns:
            The direction and position vectors as arrays.
        """
        return f'Line3D(' \
               f'position=<{self.position.x}, {self.position.y}, {self.position.z}>, ' \
               f'direction=<{self.direction.x}, {self.direction.y}, {self.direction.z}>' \
               f')'

    def __str__(self):
        """
        Converts this Line3D into a string.

        Returns:
            The direction and position vectors as arrays.
        """
        return repr(self)

    def x(self, t):
        """
        The parametric equation for the x-coordinate of this line.

        Parameters:
            t (float): The time parameter for this line

        Returns:
            float: The x-coordinate on this line at time t
        """
        return (t * self.a) + self.x0

    def y(self, t):
        """
        The parametric equation for the y-coordinate of this line.

        Parameters:
            t (float): The time parameter for this line

        Returns:
            float: The y-coordinate on this line at time t
        """
        return (t * self.b) + self.y0

    def z(self, t):
        """
        The parametric equation for the z-coordinate of this line.

        Parameters:
            t (float): The time parameter for this line

        Returns:
            float: The z-coordinate on this line at time t
        """
        return (t * self.c) + self.z0

    def pos(self, t):
        """
        The parametric equation for the position vector of this line.

        Parameters:
            t (float): The time parameter for this line

        Returns:
            Vector3D: The position vector on this line at time t
        """
        return Vector3D(self.x(t), self.y(t), self.z(t))
