from patterns.singleton import Singleton


def test_singleton():
    class A(Singleton):
        def __init__(self, id: int = None):
            self.id = id

    a = A(20)
    b = A()

    assert a.id == 20
    assert b.id == 20
    assert a is b
