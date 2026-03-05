class DFSearch:
    def __init__(self, connection_func):
        self.neighbours = connection_func
        self.reached = set()

    def explore(self, start_vertex):
        if start_vertex in self.reached:
            return
        self.reached.add(start_vertex)
        for vertex in self.neighbours(start_vertex):
            self.explore(vertex)

    def reset(self):
        self.reached = set()

    def reachable(self,vertex):
        return vertex in self.reached


