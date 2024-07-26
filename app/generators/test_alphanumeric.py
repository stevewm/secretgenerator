from .alphanumeric import AlphaNumeric


def test_validate_single_secret_returned():
    secret = AlphaNumeric.generate('secret')
    assert len(secret.keys()) == 1


def test_negative_length():
    secret = AlphaNumeric.generate('secret').get('secret')
    assert len(secret) == 32
    assert secret.isalnum() is True


def test_normal_length():
    secret = AlphaNumeric.generate('secret', 10).get('secret')
    assert len(secret) == 10
    assert secret.isalnum() is True


def test_large_length():
    length = 65534
    secret = AlphaNumeric.generate('secret', 65534).get('secret')
    assert len(secret) == length
    assert secret.isalnum() is True


def test_zero_length():
    secret = AlphaNumeric.generate('secret', 0).get('secret')
    assert len(secret) == 32
    assert secret.isalnum() is True


def test_special_character_name():
    name = '!@#$%^&*()_+'
    secret = AlphaNumeric.generate(name).get(name)
    assert len(secret) == 32
    assert secret.isalnum() is True
