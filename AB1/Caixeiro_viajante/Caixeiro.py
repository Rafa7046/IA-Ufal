from numpy import empty
from Route import Route

class Caixeiro:

    def __init__(self, initial_city):
            self.initial_city = initial_city
            self.border = self.initial_border()

    def initial_border(self):
        border = []
        for i in range(10):
            path = [self.initial_city, i+1]
            for j in range(1, 11):
                if j not in path:
                    path.append(j)
            path.append(self.initial_city)
            border.append(path)
        border.pop(self.initial_city-1)
        return border

    def route(self):
        counter = 0
        for paths in self.border:
            temporary_border = [Route(0, (0, self.initial_city), [], paths, 1)]
            while temporary_border is not empty:
                path = self.find_min(temporary_border)
                if path == []:
                    self.border[counter] = -1
                    break
                elif path.cities_visited == 10:
                    self.border[counter] = (path.trace, path.distance)
                    break 
                for son in path.sons:
                    new_son = Route(path.get_current_distance(), son[0], path.get_trace_value(), son[1], path.cities_visited+1)
                    if new_son.path_is_connected():
                        temporary_border.append(new_son)
                temporary_border.remove(path)
            counter += 1
        return self.get_best_route()


    def find_min(self, path):
        if path == []:
            return path
        min = (path[0]).get_current_distance()
        index = 0
        for i in range(len(path)):
            if path[i].get_current_distance() < min:
                min = path[i].get_current_distance()
                index = i
        return path[index]

    def get_best_route(self):
        index = 0
        counter = 0
        smaller = self.border[0][1]
        for path in self.border:
            if path != -1:
                if path[1] < smaller:
                    smaller = path[1]
                    index = counter
            counter += 1

        return self.border[index]
        
