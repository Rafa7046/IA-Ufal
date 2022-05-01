import numpy as np

class Metro_Grid():

    def __init__(self):
        self.Metro_Grid = [[0]*15]*15
        self.Metro_Grid[1]= 0, 9999, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32
        self.Metro_Grid[2]= 0, 11, 9999, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24
        self.Metro_Grid[3]= 0, 20, 9, 9999, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18
        self.Metro_Grid[4]= 0, 27, 16, 7, 9999, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17
        self.Metro_Grid[5]= 0, 40, 29, 20, 13, 9999, 3, 2, 21, 25, 31, 38, 27, 16, 20
        self.Metro_Grid[6]= 0, 43, 32, 22, 16, 3, 9999, 4, 23, 28, 33, 41, 30, 17, 20
        self.Metro_Grid[7]= 0, 39, 28, 19, 12, 2, 4, 9999, 22, 25, 29, 38, 28, 13, 17
        self.Metro_Grid[8]= 0, 28, 19, 15, 13, 21, 23, 22, 9999, 9, 22, 18, 7, 25, 30
        self.Metro_Grid[9]= 0, 18, 11, 10, 13, 25, 28, 25, 9, 9999, 13, 12, 12, 23, 28
        self.Metro_Grid[10]= 0, 10, 4, 11, 18, 31, 33, 29, 22, 13, 9999, 20, 27, 20, 23
        self.Metro_Grid[11]= 0, 18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 9999, 15, 35, 39
        self.Metro_Grid[12]= 0, 30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 9999, 31, 37
        self.Metro_Grid[13]= 0, 30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 9999, 5
        self.Metro_Grid[14]= 0, 32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 9999
        self.Metro_Grid = self.__generate_Metro_Grid_table(self.Metro_Grid)
        self.Lines = self.__lines()
        
    def __generate_Metro_Grid_table(self,table):
        return np.multiply(table, 2)

    def __lines(self):
        blue = [1, 2, 3, 4, 5, 6]
        red = [11, 9, 3, 13]
        green = [12, 8, 4, 13, 14]
        yellow = [7, 5, 8, 9, 2, 10]
        lines = [blue, red, green, yellow]
        return lines

    def find_neighbor_estations(self, estation, line, last_estation):
        neighbors = []
        for i in range(4):
            k = 0
            for j in self.Lines[i]:
                if j == estation:
                    if line != i:
                        extra_time = 4
                    else:
                        extra_time = 0
                    if k+1 < len(self.Lines[i]):
                        neighbors.append((self.Lines[i][k+1], extra_time, i))
                    if k-1 >= 0:
                        neighbors.append((self.Lines[i][k-1], extra_time, i))
                k += 1
        operators = []
        for i in neighbors:
            if last_estation != i[0] or len(neighbors) == 1:
                operators.append((estation, i[0], i[1], i[2]))
        return operators
