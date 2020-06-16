import pytest


@pytest.mark.parametrize("input_str, expected_str", [
        pytest.param("abC", "abc", id="this is test 1"),
        pytest.param("aBC", "abc", id="这是测试用例2")
    ]
)
def test_remove_whitespaces(input_str, expected_str):
    assert input_str == expected_str


# https://github.com/pytest-dev/pytest/pull/1463/files