from numpy import empty
from Metro import Metro
from Metro_Grid import Metro_Grid

class Passenger():

    def __init__(self, initial_station, final_station):
        self.initial_station = initial_station
        self.final_station = final_station
        self.border = self.initial_border()

    def initial_border(self):
        lines = []
        border = []
        for i in range(4):
            for j in Metro_Grid().Lines[i]:
                if j == self.initial_station:
                    lines.append(i)
        for i in lines:
            border.append(Metro(-1, 0, [], (-1, self.initial_station, 0, i, -1), []))

        return border

    def route(self):
        while self.border is not empty:
            metro = self.find_min()
            if metro.operator[1] == self.final_station:
                    return (metro.trace, metro.time, self.metro_connections(metro.connections))
            for i in metro.sons:
                new_son = Metro(metro.get_current_station(), metro.get_current_time(), metro.get_trace_value(), i, metro.get_connections_value())
                self.border.append(new_son)
            self.border.remove(metro)

    def find_min(self):
        min = (self.border[0]).get_current_time()
        index = 0
        for i in range(len(self.border)):
            if self.border[i].get_current_time() < min:
                min = self.border[i].get_current_time()
                index = i
        return self.border[index]

    def metro_connections(self, connections_list):
        connections = []
        for i in connections_list:
            if i != -1:
                connections.append(i)
        
        return connections

    def line_name(self, line):
        names = ["azul", "vermelha", "verde", "amarela"]
        return names[line]
