import pytest
from ch02.or_gate import OR


@pytest.mark.parametrize(
    "x1, x2, expected_value", [
        (0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)
    ]
)
def test_OR(x1, x2, expected_value):
    assert OR(x1, x2) == expected_value
