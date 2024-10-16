def test_equal_or_not_equal():
    assert 1 == 1
    assert 1 != 3


def test_is_instance():
    assert isinstance('This is a str', str)
    assert isinstance(1, int)


def test_boolean():
    validate = True
    assert validate is True
    assert ('hello world' == 'hello rifayte') is False


def test_type():
    assert type('hello' is str)
    assert type('hello' is not int)


def test_greter_and_less_than():
    assert 2 > 1
    assert 4 < 10


def test_list():
    num_list = [1, 2, 3]
    any_list = [False, False]

    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)