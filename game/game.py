import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

X_SIZE = 4
Y_SIZE = 4
N_ITER = 100

INITIAL_STATE = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)


def generate_initial_state(x_size, y_size):
    pass


def safe_index(array, ix, iy):
    if ix < 0 or iy < 0:
        return 0
    try:
        return array[ix, iy]
    except IndexError:
        return 0


def count_alive_neighbors(state, ix, iy):
    neighbors = [
        safe_index(state, ix - 1, iy - 1),
        safe_index(state, ix - 1, iy),
        safe_index(state, ix - 1, iy + 1),
        safe_index(state, ix, iy - 1),
        safe_index(state, ix, iy + 1),
        safe_index(state, ix + 1, iy - 1),
        safe_index(state, ix + 1, iy),
        safe_index(state, ix + 1, iy + 1),
    ]
    return sum(neighbors)


def alive_or_dead(state, ix, iy):
    n_alive_neighbors = count_alive_neighbors(state, ix, iy)
    is_alive = 0
    if state[ix, iy] == 0 and n_alive_neighbors >= 3:
        is_alive = 1
    elif state[ix, iy] == 1 and n_alive_neighbors >= 2:
        is_alive = 1
    return is_alive


def update_state(state):
    new_state = np.zeros_like(state)
    for ix in range(state.shape[0]):
        for iy in range(state.shape[1]):
            new_state[ix, iy] = alive_or_dead(state, ix, iy)
    return new_state


def run_game(x_size, y_size, n_iter):
    all_states = [INITIAL_STATE]
    for iter in range(n_iter):
        all_states.append(update_state(all_states[iter]))
    return all_states


if __name__ == '__main__':

    states = run_game(X_SIZE, Y_SIZE, N_ITER)
    fig = plt.figure()
    plot = plt.imshow(states[0])

    def init():
        plot.set_data(states[0])
        return [plot]


    def update(j):
        plot.set_data(states[j])
        return [plot]

    anim = FuncAnimation(fig, update, init_func=init, frames=len(states), interval=500, blit=True)
    plt.show()