from somefile import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -10, -3),
                                                   (5, 2, 2.5)])
def test_division_ok(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expexted_error, a, b", [(ZeroDivisionError, 10, 0),
                                                  (TypeError, 10, '2')])
def test_division_with_error(expexted_error, a, b):
    with pytest.raises(expexted_error):
        division(a, b)
