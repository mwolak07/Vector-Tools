from src.utils_3d import Utils3D


class Plane3D:
    """
    Represents a plane in three dimensions. Uses the position vector p and normal vector n to define the plane.

    Represents the following equation: 
    ax + by + cz = d

    Notes:
        - Implements as many operations as possible with efficient numpy functions.

    Attributes:
        position (Vector3D): Represents the position vector for this plane.
        normal (Vector3D): Represents the normal vector for this plane.
        a (float): Represents the x coefficient in the formula.
        b (float): Represents the y coefficient in the formula.
        c (float): Represents the z coefficient in the formula.
        d (float): Represents the sum coefficient in the formula.
    """

    def __init__(self, position, normal):
        """
        Initializes a new Plane3D using a point p and normal vector n.
        
        Computes a, b, c, and d based on p and n.

        Args:
            position (Vector3D): The position vector for this plane.
            normal (Vector3D): The normal vector for this plane.
        """
        self.position = position
        self.normal = normal
        self.a = self.normal.x
        self.b = self.normal.y
        self.c = self.normal.z
        self.d = (self.normal.x * self.position.x) + \
                 (self.normal.y * self.position.y) + \
                 (self.normal.z * self.position.z)

    @classmethod
    def from_two_lines(cls, a, b):
        """
        Initializes a Plane3D defined by two lines.

        Uses the position vector of a as p, and the cross product of the a and b direction vectors as n.

        Args:
            a (Line3D): The first line defining this plane.
            b (Line3D): The second line defining this plane.
        """
        return cls(a.position, Utils3D.cross(a.direction, b.direction))

    # TODO
    @classmethod
    def from_three_points(cls, a, b, c):
        pass

    def __repr__(self):
        """
        Converts this Plane3D into a human-readable representation

        Returns:
            The direction and position vectors as arrays.
        """
        return f'Plane3D(' \
               f'position=<{self.position.x}, {self.position.y}, {self.position.z}>, ' \
               f'normal=<{self.normal.x}, {self.normal.y}, {self.normal.z}>' \
               f')'

    def __str__(self):
        """
        Converts this Plane3D into a string.

        Returns:
            The position and normal vectors as arrays.
        """
        return repr(self)

    def x(self, y, z):
        """
        Gets the x-coordinate on the plane given the y and z coordinates.

        Solves the following equation through substitution: 
        0 = n.x(x - p.x) + n.y(y - p.y) + n.z(z - p.z)

        Args:
            y (double): The y-coordinate on the plane.
            z (double): The z-coordinate on the plane.
        
        Returns:
            float: The corresponding x-coordinate on the plane.
        """
        return (((self.normal.y * (y - self.position.y)) +
                 (self.normal.z * (z - self.position.z))) / (-1 * self.normal.x)) + self.position.x

    def y(self, x, z):
        """
        Gets the y-coordinate on the plane given the x and z coordinates.

        Solves the following equation through substitution: 
        0 = n.x(x - p.x) + n.y(y - p.y) + n.z(z - p.z)

        Args:
            x (double): The x-coordinate on the plane.
            z (double): The z-coordinate on the plane.
        
        Returns:
            float: The corresponding y-coordinate on the plane.
        """
        return (((self.normal.x * (x - self.position.x)) +
                 (self.normal.z * (z - self.position.z))) / (-1 * self.normal.y)) + self.position.y

    def z(self, x, y):
        """
        Gets the z-coordinate on the plane given the x and y coordinates.

        Solves the following equation through substitution: 
        0 = n.x(x - p.x) + n.y(y - p.y) + n.z(z - p.z)

        Args:
            x (double): The x-coordinate on the plane.
            y (double): The y-coordinate on the plane.
        
        Returns:
            float: The corresponding z-coordinate on the plane.
        """
        return (((self.normal.x * (x - self.position.x)) +
                 (self.normal.y * (y - self.position.y))) / (-1 * self.normal.z)) + self.position.z
