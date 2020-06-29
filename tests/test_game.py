from game.game import count_alive_neighbors, INITIAL_STATE


def test_count_alive_neighbors(init_5x5_oscillator):
    assert count_alive_neighbors(init_5x5_oscillator, 0, 0) == 0
    assert count_alive_neighbors(init_5x5_oscillator, 2, 2) == 2
    assert count_alive_neighbors(init_5x5_oscillator, 1, 1) == 2
    assert count_alive_neighbors(init_5x5_oscillator, 1, 2) == 3
    assert count_alive_neighbors(init_5x5_oscillator, 2, 1) == 1
