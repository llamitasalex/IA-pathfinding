from States import State


def search(algorithm, origin, solution, map):
    map.map[origin.x][origin.y] = 3
    map.draw(origin.x, origin.y)
    map.map[solution.final_state.x][solution.final_state.y] = 4
    map.draw(solution.final_state.x, solution.final_state.y)

    # La lista de caminos pendientes se inicia con el estado origen.
    cp = [[origin]]

    # Repetimos el algoritmo mientras haya caminos pendientes.
    while cp:

        # Cogemos el primer camino de la lista de caminos pendientes
        path = cp.pop(0)

        if solution(path):
            # Genial, hemos terminado
            return path
        else:
            # Vaya, seguimos buscando por los sucesores. Expandimos...
            last_state = path[-1]
            if map.map[last_state.x][last_state.y] != 2:
                map.map[last_state.x][last_state.y] = 3
                map.draw(last_state.x, last_state.y)
                map.map[last_state.x][last_state.y] = 2
                map.draw(last_state.x, last_state.y)
            e = []
            for state in last_state.successors():
                if state not in path and map.map[state.x][state.y] != 2:  # Así evitamos caminos cíclicos
                    expansion = path + [state]
                    e.append(expansion)
            # ... y concatenamos según diga el algoritmo
            cp = algorithm(cp, e)

    # Si hemos salido del bucle, es porque no había ningún camino que
    # llegase al resultado
    return False


class MapSolution:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Solution:

    def __init__(self, m, x, y):
        self.final_state = State(m, x, y)

    def __call__(self, path_aux):
        last_state = path_aux[-1]
        return self.final_state == last_state


def print_path(path, cost=None, heuristic=None):
    if path:
        for i, state in enumerate(path, 1):
            msg = f'Step {i} \t[{state}]'
            if heuristic:
                msg += f' heuristic = {heuristic(state)}'
            print(msg)
        if cost:
            print(f'Cost = {cost(path)}')
    else:
        print('No existe')
