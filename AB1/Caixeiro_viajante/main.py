from Caixeiro import Caixeiro

def main():
    initial_city = int(input(f"Digite a cidade inicial como um número de 1 a 10: "))
    caixeiro = Caixeiro(initial_city)
    path = caixeiro.route()
    print("\n----------------------------------------------------------------------------------------------------\n")
    
    print(f"O caminho mais curto é {path[0]} e levará {path[1]} quilômetros")

    print("\n----------------------------------------------------------------------------------------------------\n")

main()