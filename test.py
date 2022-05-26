import pytest
from main import encode, decode


@pytest.mark.parametrize(
    "input,expected_output",
    [
        ("", ""),
        ("ABC", "ABC"),
        ("DDDDDAABBBCCCC", "5D2A3B4C"),
        ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB", "12WB12W3B24WB"),
        ("  hsqq qww  ", "2 hs2q q2w2 "),
        ("aabbbcccc", "2a3b4c"),
    ],
)
def test_encode(input, expected_output):
    assert encode(input) == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [
        ("", ""),
        ("ABC", "ABC"),
        ("5D2A3B4C", "DDDDDAABBBCCCC"),
        ("10WB12W3B24WB", "WWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"),
        ("2 hs2q q2w2 ", "  hsqq qww  "),
        ("2a3b4c", "aabbbcccc"),
    ],
)
def test_decode(input, expected_output):
    assert decode(input) == expected_output
