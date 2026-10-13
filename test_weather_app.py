
from weather_app import describe_weather


def test_clear_sky():
    assert describe_weather(0) == "Clear sky"


def test_rain():
    assert describe_weather(63) == "Moderate rain"


def test_unknown_weather():
    assert describe_weather(999) == "Unknown conditions"


if __name__ == "__main__":
    test_clear_sky()
    test_rain()
    test_unknown_weather()
    print("All tests passed!")