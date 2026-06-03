def test_valid_token(): assert verify('valid') == {'sub': 'user1'}
def test_invalid_token(): assert verify('bad') is None
