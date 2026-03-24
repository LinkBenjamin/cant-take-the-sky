import pytest

from app.models.hero import Hero

def test_gain_xp():
    a = {
        "name":"test",
        "nickname": "t",
        "level":1,
        "special":"s",
        "attributes":{
            "one":1,
            "two":2,
            "three":3
        }
    }
    x = Hero("image", a)

    x.gain_xp(100,"one")
    assert x.level == 1
    assert x.xp == 100
    assert x.xp_uses == ["one"]

    x.gain_xp(1000, "one")
    assert x.level == 2
    assert x.xp == 100
    assert x.xp_uses == []
    assert x.attributes["one"] == 11

