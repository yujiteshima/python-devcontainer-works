import pytest
from ch02.and_gate import AND


@pytest.mark.parametrize(
    "x1, x2, expected_value", [
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1)
    ]
)
def test_AND(x1, x2, expected_value):
    assert AND(x1, x2) == expected_value
