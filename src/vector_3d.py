from numpy.linalg import norm as np_norm
from numpy import array as np_array


class Vector3D:
    """
    Represents a vector in three dimensions, starting at the origin. This can represent a position or direction.

    Notes:
        - Implements as many operations as possible with efficient numpy functions.

    Attributes:
        x (float): Represents the coefficient for the i unit vector (x coordinate).
        y (float): Represents the coefficient for the j unit vector (y coordinate).
        z (float): Represents the coefficient for the k unit vector (z coordinate).
        np_vec (np.ndarray(float)): Represents the vector as a 3x1 numpy array.
    """

    def __init__(self, x, y, z):
        """
        Initializes a new Vector3D from the x, y, and z components.

        Computes np_vec from x, y, and z.

        Args:
            x (float): The x component of the vector.
            y (float): The y component of the vector.
            z (float): The z component of the vector.
        """
        self.x = x
        self.y = y
        self.z = z
        self.np_vec = np_array([self.x, self.y, self.z])

    @classmethod
    def from_numpy(cls, np_vec):
        """
        Initializes a Vector3D from a (3,) numpy array.

        Args:
            np_vec (np.array(float)): The position vector for the first point.
            
        Raises:
            ValueError: When np_vec is not of shape (3,).
        """
        if np_vec.shape == (3,):
            return cls(np_vec[0], np_vec[1], np_vec[2])
        else:
            raise ValueError("input vector of shape {shape} does not have correct shape of (3,)."
                             .format(shape=np_vec.shape))

    def __repr__(self):
        """
        Converts this Vector3D into a human-readable representation

        Returns:
            The direction and position vectors as arrays.
        """
        return f'Plane3D(' \
               f'<x={self.x}, y={self.y}, z={self.z}>' \
               f')'

    def __str__(self):
        """
        Converts this Vector3D into a string.

        Returns:
            The direction vector as an array.
        """
        return repr(self)

    def __add__(self, other):
        """
        Adds the vector other to this vector.

        Args:
            other (Vector3D): The other vector.

        Returns:
            Vector3D: The result, this + other.

        Raises:
            TypeError: When other is not a Vector3D.
        """
        if isinstance(other, Vector3D):
            return Vector3D.from_numpy(self.np_vec + other.np_vec)
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __sub__(self, other):
        """
        Subtracts the vector other from this vector.

        Args:
            other (Vector3D): The other vector.

        Returns:
            Vector3D: The result, this - other.

        Raises:
            TypeError: When other is not a Vector3D.
        """
        if isinstance(other, Vector3D):
            return Vector3D.from_numpy(self.np_vec - other.np_vec)
        else:
            raise TypeError("unsupported operand type(s) for -: 't_type' and '{o_type}'"
                            .format(t_type=type(self), o_type=type(other)))

    def __mul__(self, s):
        """
        Multiplies this vector by a scalar s.

        Args:
            s (float, int): The scalar to multiply by.

        Returns:
            Vector3D: The result, this * s.

        Raises:
            TypeError: When other is not a float or int.
        """
        if isinstance(s, float) or isinstance(s, float):
            return Vector3D.from_numpy(s * self.np_vec)
        else:
            raise TypeError("unsupported operand type(s) for *: 't_type' and '{s_type}'"
                            .format(t_type=type(self), s_type=type(s)))

    def norm(self):
        """
        Gets the norm, or magnitude, of this vector.

        Returns:
            The norm of this vector.
        """
        return np_norm(self.np_vec)

    def normalized(self):
        """
        Normalizes this vector, so that it has a length of 1.

        Returns:
            A normalized version of this vector.
        """
        return Vector3D.from_numpy(self.np_vec / self.norm())
