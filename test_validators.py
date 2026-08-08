from validators import is_valid_email


def test_accepts_a_normal_address():
    assert is_valid_email("person@example.com")


def test_rejects_missing_at_sign():
    assert not is_valid_email("not-an-email")


def test_rejects_empty_string():
    assert not is_valid_email("")
