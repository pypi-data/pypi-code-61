from okdoodle import sayhello

def test_okdoodle_no_params():
    assert sayhello() == "Hello, world!"

def test_okdoodle_with_params():
    assert sayhello("Everybody") == "Hello, Everybody!"