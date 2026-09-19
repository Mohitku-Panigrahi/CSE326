import heapq

goal_state = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

start_state = (
    1, 5, 2,
    4, 3, 0,
    7, 8, 6
)


def calculate_manhattan_distance(state):

    distance = 0

    for index, tile in enumerate(state):

        if tile != 0:

            goal_index = tile - 1

            distance += abs(index // 3 - goal_index // 3)
            distance += abs(index % 3 - goal_index % 3)

    return distance


def generate_neighbors(state):

    blank_index = state.index(0)

    row, column = divmod(blank_index, 3)

    neighbors = []

    for row_move, column_move in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:

        new_row = row + row_move
        new_column = column + column_move

        if 0 <= new_row < 3 and 0 <= new_column < 3:

            new_index = new_row * 3 + new_column

            new_state = list(state)

            new_state[blank_index], new_state[new_index] = (
                new_state[new_index],
                new_state[blank_index]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def hill_climbing(start):

    current_state = start

    steps = 0

    while current_state != goal_state:

        best_neighbor = min(
            generate_neighbors(current_state),
            key=calculate_manhattan_distance
        )

        if calculate_manhattan_distance(best_neighbor) >= calculate_manhattan_distance(current_state):
            return False, steps

        current_state = best_neighbor
        steps += 1

    return True, steps


solved, steps = hill_climbing(start_state)

print("Hill Climbing")
print("Solved :", solved)
print("Steps  :", steps)

def a_star_search(start):

    priority_queue = [
        (
            calculate_manhattan_distance(start),
            0,
            start
        )
    ]

    visited_states = set()

    while priority_queue:

        total_cost, path_cost, current_state = heapq.heappop(
            priority_queue
        )

        if current_state == goal_state:
            return path_cost

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        for neighbor_state in generate_neighbors(current_state):

            new_path_cost = path_cost + 1

            heapq.heappush(
                priority_queue,
                (
                    new_path_cost +
                    calculate_manhattan_distance(neighbor_state),
                    new_path_cost,
                    neighbor_state
                )
            )

    return -1


steps = a_star_search(start_state)

print("A* Search")
print("Steps :", steps) 
# i was absent 