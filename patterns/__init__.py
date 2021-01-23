from pytest import (fixture, mark, raises, main, yield_fixture, PytestWarning,
                    PytestUnknownMarkWarning, PytestCollectionWarning)


def test(test: int, number: int, d):
    pass


test(1, 2, 3)
