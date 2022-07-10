import pytest
from ch02.nand_gate import NAND


@pytest.mark.parametrize(
    "x1, x2, expected_value", [
        (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 0)
    ]
)
def test_NAND(x1, x2, expected_value):
    assert NAND(x1, x2) == expected_value
