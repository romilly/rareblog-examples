from plotting.display import Pen


class Matrix:
    """A simple 2D matrix implementation with row and column indexing."""

    def __init__(self, width: int, height: int):
        """
        Initialize a matrix with specified width and height.

        Args:
            width: Number of columns in the matrix
            height: Number of rows in the matrix
        """
        self.width = width
        self.height = height
        # Initialize the matrix with None values
        self._data = [[Pen(0,0,0) for _ in range(width)] for _ in range(height)]

    def __getitem__(self, index) -> Pen:
        x, y = index
        return self._data[y][x]

    def __setitem__(self, index, value:Pen):
        x, y = index
        self._data[y][x] = value

    def __str__(self):
        """Return a string representation of the matrix."""
        return "\n".join([" ".join([str(item) for item in row]) for row in self._data])

    def __repr__(self):
        """Return a formal string representation of the matrix."""
        return f"Matrix({self.width}, {self.height})"