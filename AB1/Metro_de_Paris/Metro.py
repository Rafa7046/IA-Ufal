from Metro_Grid import Metro_Grid

class Metro():
    
    def __init__(self, last_station, time, trace, operator, connections):
        self.operator = operator
        self.time = self.travel_time(time)
        self.last_station = last_station
        self.trace = trace
        self.trace.append(self.operator[1])
        self.sons = self.paths()
        self.connections = connections
        self.connections.append(self.operator[4])

    def get_current_station(self):
        return self.operator[1]

    def get_current_time(self):
        return self.time

    def get_trace_value(self):
        return list(self.trace)

    def get_connections_value(self):
        return list(self.connections)

    def paths(self):
        metro_grid = Metro_Grid()
        operators = metro_grid.find_neighbor_estations(self.operator[1], self.operator[3], self.last_station)
        return operators

    def travel_time(self, time):
        if self.operator[0] != -1:
            return time + self.operator[2] + Metro_Grid().Metro_Grid[self.operator[0]][self.operator[1]]
        else: 
            return 0
