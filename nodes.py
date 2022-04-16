from ast import Pass


class Nodes():

    def __init__(self, current_state, trace, operator=1):
        self.current_state = current_state
        self.operator = operator
        self.sons = []
        self.trace = trace
        self.trace.append(self.current_state)

    def get_state_value(self):
        return list(self.current_state)

    def get_trace_value(self):
        return list(self.trace)

    def generate_sons(self):
        operators = []
        if self.current_state[4] == 0:
            if self.current_state[0] >= 2:
                operators.append((2,0))
            if self.current_state[0] >= 1:
                operators.append((1,0))
            if self.current_state[0] >= 1 and self.current_state[1] >= 1:
                operators.append((1,1))
            if self.current_state[1] >= 2:
                operators.append((0,2))
            if self.current_state[1] >= 1:
                operators.append((0,1))
        else:
            if self.current_state[2] >= 2:
                operators.append((2,0))
            if self.current_state[2] >= 1:
                operators.append((1,0))
            if self.current_state[2] >= 1 and self.current_state[3] >= 1:
                operators.append((1,1))
            if self.current_state[3] >= 2:
                operators.append((0,2))
            if self.current_state[3] >= 1:
                operators.append((0,1))
        self.sons = operators


    def move (self):
        if self.current_state[4] == 0:
            if(self.operator == (0,1)):
                self.current_state[1] -= 1
                self.current_state[3] += 1
            elif(self.operator == (0,2)):
                self.current_state[1] -= 2
                self.current_state[3] += 2
            if(self.operator == (1,1)):
                self.current_state[0] -= 1
                self.current_state[1] -= 1
                self.current_state[2] += 1
                self.current_state[3] += 1
            elif(self.operator == (1,0)):
                self.current_state[0] -= 1
                self.current_state[2] += 1
            elif(self.operator == (2,0)):
                self.current_state[0] -= 2
                self.current_state[2] += 2
            self.current_state[4] = 1
        else:
            if(self.operator == (0,1)):
                self.current_state[1] += 1
                self.current_state[3] -= 1
            elif(self.operator == (0,2)):
                self.current_state[1] += 2
                self.current_state[3] -= 2
            elif(self.operator == (1,1)):
                self.current_state[0] += 1
                self.current_state[1] += 1
                self.current_state[2] -= 1
                self.current_state[3] -= 1
            elif(self.operator == (1,0)):
                self.current_state[0] += 1
                self.current_state[2] -= 1
            elif(self.operator == (2,0)):
                self.current_state[0] += 2
                self.current_state[2] -= 2
            self.current_state[4] = 0
