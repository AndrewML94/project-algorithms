import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 'key')

    assert encrypt_message('undefined', 10) == 'denifednu'
    assert encrypt_message('typescript', 4) == 'tpircs_epyt'
    assert encrypt_message('react', 1) == 'r_tcae'
