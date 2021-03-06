class Map():

    def __init__(self):
        self.map = [[0]*11]*11
        self.map[1] = 0, -1, 30, 84, 56, -1, -1, -1, 75, -1, 80
        self.map[2] = 0, 30, -1, 65, -1, -1, -1, 70, -1, -1, 40
        self.map[3] = 0, 84, 65, -1, 74, 52, 55, -1, 60, 143, 48
        self.map[4] = 0, 56, -1, 74, -1, 135, -1, -1, 20, -1, -1
        self.map[5] = 0, -1, -1, 52, 135, -1, 70, -1, 122, 98, 80
        self.map[6] = 0, 70, -1, 55, -1, 70, -1, 63, -1, 82, 35
        self.map[7] = 0, -1, 70, -1, -1, -1, 63, -1, -1, 120, 57
        self.map[8] = 0, 75, -1, 135, 20, 122, -1, -1, -1, -1, -1
        self.map[9] = 0, -1, -1, 143, -1, 98, 82, 120, -1, -1, -1
        self.map[10] = 0, 80, 40, 48, -1, 80, 35, 57, -1, -1, -1

    def is_connected(self, path, cities):
        for i in range(cities-1):
            if self.map[path[i]][path[i+1]] == -1:
                return 0
        return 1
