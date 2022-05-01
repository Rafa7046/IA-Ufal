from Passenger import Passenger

def main():
    initial_station = int(input(f"Digite a estação inicial como um número de 1 a 14: "))
    final_station = int(input(f"Informe a estação de destino como um número de 1 a 14: "))
    passanger = Passenger(initial_station, final_station)
    path = passanger.route()
    print("\n----------------------------------------------------------------------------------------------------\n")
    
    print(f"O caminho mais curto é {path[0]} e levará {path[1]} minutos")
    for i in path[2]:
        print(f"Conexão na estação {i[0]} da linha {passanger.line_name(i[1])} para a linha {passanger.line_name(i[2])}.")

    print("\n----------------------------------------------------------------------------------------------------\n")

main()