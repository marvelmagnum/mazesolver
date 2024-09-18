class Line:
    def __init__(self, point_a, point_b):
        self.start = point_a
        self.end = point_b

    def draw(self, canvas, color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)
        