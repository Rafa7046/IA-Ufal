from nodes import Nodes

def main():
    initial_state = [3, 3, 0, 0, 0]
    border = []
    first_node = Nodes(initial_state, [])
    first_node.generate_sons()
    border.append(first_node)
    for node in border:
        # print(node.current_state)
        if node.current_state == [0,0,3,3,1]:
                print(node.trace)
                print(f"Caminho encontrado")
                return
        for operator in node.sons:
            new_son = Nodes(node.get_state_value(), node.get_trace_value(), operator)
            new_son.move()
            if (((new_son.current_state[1] <= new_son.current_state[0]) or new_son.current_state[0] == 0) and ((new_son.current_state[3] <= new_son.current_state[2]) or new_son.current_state[2] == 0)):
                new_son.generate_sons()
                border.append(new_son)

main()
        

