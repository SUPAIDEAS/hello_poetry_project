from hello.main import get_me_hello


def test_say_hello(monkeypatch):
    output = get_me_hello()
    assert output == 'Hello'
