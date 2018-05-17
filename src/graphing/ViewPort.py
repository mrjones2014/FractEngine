from Point2D import Point2D, distance

class ViewPort:
    def __init__(self, top_left: Point2D, bottom_right: Point2D, dpi: int):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.dpi = dpi
    
    @property
    def diagonal_distance(self):
        return distance(self.top_left, self.bottom_right)