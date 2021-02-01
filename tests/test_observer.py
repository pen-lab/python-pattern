import pytest

from patterns.observer import Observer, Subject


class Display:
    _echo: str

    def display(self) -> str:
        return self._echo


class WeatherData(Subject):
    def __init__(self):
        self._observers = []


@pytest.fixture
def weather_data() -> Subject:
    return WeatherData()


class StatisticDisplay(Observer, Display):
    def __init__(self):
        self._stat = []
        self._echo = ''

    def update(self, data):
        self._stat.append(data)
        self._echo = f'Max: {max(self._stat)}'


@pytest.fixture
def statistics_display() -> Observer:
    return StatisticDisplay()


def test_register(statistics_display: StatisticDisplay, weather_data: WeatherData):
    weather_data.register(statistics_display)
    assert statistics_display in weather_data._observers

    weather_data.notify(10)
    weather_data.notify(-12)
    weather_data.notify(-2)

    assert statistics_display.display() == 'Max: 10'


# TODO: удаление элемента, добавление нескольких, нагрузка, добавление одинаковых, типизация