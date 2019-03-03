from sq_dict import sq_func


def test_sq_func_return_dict():
    result = sq_func()
    assert isinstance(result, dict)


def test_sq_func_has_sq_4():
    result = sq_func()
    assert result[2] == 4
