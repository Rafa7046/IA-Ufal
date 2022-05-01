from A_star_search import route

def main():
    initial_station = int(input(f"Digite a estação inicial como um número de 1 a 14: "))
    line = int(input(f"Informe a linha que você está \n [0] Azul \n [1] Vermelha \n [2] Verde \n [3] Amarela \n"))
    final_station = int(input(f"Informe a estação de destino como um número de 1 a 14: "))
    path = route(initial_station, line, final_station)
    print(f"O caminho mais curto é {path[0]} e levará {path[1]} minutos")

main()