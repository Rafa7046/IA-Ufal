from Map import Map

class Route:

    def __init__(self, distance, operator, trace, path, cities_visited):
        self.operator = operator
        self.trace = trace
        self.trace.append(self.operator[1])
        self.path = path
        self.cities_visited = cities_visited
        self.distance = self.travel_distance(distance)
        self.sons = self.generate_sons()

    def get_current_distance(self):
        return self.distance

    def get_trace_value(self):
        return list(self.trace)

    def travel_distance(self, distance):
        return distance + Map().map[self.operator[0]][self.operator[1]]

    def generate_sons(self):
        sons = []
        counter = self.cities_visited
        if self.cities_visited > 1:
            while  counter < 10:
                current_path = self.path[:]
                current_path[self.cities_visited], current_path[counter] = current_path[counter], current_path[self.cities_visited]
                sons.append([(current_path[self.cities_visited - 1], current_path[self.cities_visited]), current_path[:]])
                counter += 1
        else:
            sons.append([(self.path[self.cities_visited - 1], self.path[self.cities_visited]), self.path[:]])
        return sons

    def path_is_connected(self):
        return Map().is_connected(self.path, self.cities_visited)

# x = Route(30, (1, 2), [], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], 1)
# for i in x.sons:
#     print(i)


    

