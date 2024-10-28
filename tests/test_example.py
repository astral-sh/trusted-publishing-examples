from trusted_publishing_examples import hello


def test_hello():
    assert hello(0) == "Hello 0!"
    assert hello(1) == "Hello 0!"
    assert hello(1000) == "Hello 499500!"
