import pytest

from diversos.closest_enemy import closest_enemy


@pytest.mark.parametrize(
    'positions, expected',
    (
        ([1], 0),
        ([0, 0, 1, 0, 2], 2),
        ([2, 0, 0, 0, 1, 0, 0, 2], 3),
        ([2, 1, 0, 0, 0, 0, 2], 1),
        ([1, 0, 0, 0, 2], 4),
        ([0, 2, 0, 0, 1], 3)
    )
)
def test_enemies(positions, expected):
    res = closest_enemy(positions)
    assert res == expected