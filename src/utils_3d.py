from numpy import cross as np_cross
from numpy import dot as np_dot


class Utils3D:
    """
    Contains a collection of utility functions for doing various operations with Vector3D, Line3D, and Plane3D.

    Notes:
        - Implements as many operations as possible with efficient numpy functions.
    """

    @staticmethod
    def cross(a, b):
        """
        Gets the cross product of two Vector3Ds.

        computed using the matrix as follows:
        a x b = | i   j   k | = (a.y*b.z - a.z*b.y) i,
                |a.x a.y a.z|   (a.z*b.x - a.x*b.z) j,
                |b.x b.y b.z|   (a.x*b.y - a.y*b.x) k
        This is done with numpy for speed.

        Args:
            a (Vector3D): The first vector.
            b (Vector3D): The second vector.

        Returns:
            Vector3D: The cross product of a and b (perpendicular to both).
        """
        return np_cross(a.np_vec, b.np_vec)

    @staticmethod
    def dot(a, b):
        """
        Gets the dot product of two Vector3Ds.

        Computed as follows:
        a . b = a.x*b.x + a.y*b.y + a.z*b.z
        This is done with numpy for speed.

        Args:
            a (Vector3D): The first vector.
            b (Vector3D): The second vector.

        Returns:
            float: The dot product of a and b.
        """
        return np_dot(a.np_vec, b.np_vec)

    @staticmethod
    def intersect_line_plane(line, plane):
        """
        Gets the position Vector3D at which given line intersects the given plane.

        Computed by substituting the parametric equations for the line into x, y, and z in the equation for the plane,
        and solving for t. Then, t is substituted back into the parametric equation for the line to get the position
        vector for the intersection point.

        Plane equation: D = Ax + By + Cz
        Line equations: x = at + x0
                        y = bt + y0
                        z = ct + z0

        Args:
            line (Line3D): The line we are using.
            plane (Plane3D): The plane we are using.

        Returns:
            Vector3D: A position vector representing the point of intersection.

        Raises:
            NoSolutionError: When the line and plane do not intersect.
            InfiniteSolutionError: When the line lies within the plane.
        """
        # Substituting line equation into plane equation and solving for t:
        # D = A(at + x0) + B(bt + y0) + C(ct + z0)
        # D = t(Aa + Bb + Cc) + Ax0 + By0 + Cz0
        # D = t(t_term) + const_term
        t_term = (plane.a * line.a) + (plane.b * line.b) + (plane.c * line.c)
        const_term = (plane.a * line.x0) + (plane.b * line.y0) + (plane.c * line.z0)
        # If t_term != 0, we can solve for t:
        # t = (D - const_term) / t_term
        if t_term != 0:
            t = (plane.d - const_term) / t_term
            return line.pos(t)
        # If t_term = 0 and D != const_term, we have no solution.
        elif t_term == 0 and plane.d != const_term:
            raise NoSolutionError('the line does not intersect the plane')
        # If t_term = 0 and D = const_term, we have infinite solutions.
        elif t_term == 0 and plane.d == const_term:
            raise InfiniteSolutionError('the line lies within the plane')


class NoSolutionError(ArithmeticError):
    """
    Error to be raised when there is no solution for an operation.
    """
    pass


class InfiniteSolutionError(ArithmeticError):
    """
    Error to be raised when there are infinite solutions to an operation.
    """
    pass
