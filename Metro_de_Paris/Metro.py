from Metro_Grid import Metro_Grid

class Metro():
    
    def __init__(self, origin, line, last_station):
        self.current_estation = origin
        self.time = 0
        self.current_line = line
        self.last_station = last_station

    def paths(self):
        metro_grid = Metro_Grid()
        operators = metro_grid.find_neighbor_estations(self.current_estation, self.current_line, self.last_station)
        print(operators)

