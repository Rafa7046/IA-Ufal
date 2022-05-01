from numpy import empty
from Metro import Metro

def A_star_search(border, final_station):
    while border is not empty:
        min = border[0].get_current_time()
        index = 0
        for i in range(len(border)):
            if border[i].get_current_time() < min:
                min = border[i].get_current_time()
                index = i
        metro = border[index]
        if metro.operator[0] == final_station:
                metro.trace.pop(0)
                return (metro.trace, metro.time)
        for i in metro.sons:
            new_son = Metro(metro.get_current_station(), metro.get_current_time(), metro.get_trace_value(), i)
            border.append(new_son)
        border.remove(metro)

def route(initial_station, line, final_station):
    initial_operator = (-1, initial_station, 0, line)
    border = []
    first_metro = Metro(-1, 0, [], initial_operator)
    border.append(first_metro)
    return A_star_search(border, final_station)