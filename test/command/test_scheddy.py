from command import scheddy_plus


def run_test():
    test_data = {
        "is_this_week": {
            "data": "17/01/20",
            "monday": "13/01/20",
            "expected": True
        }
    }

    for item in test_data.is_this_week:
        actual = test_is_this_week(item.data)
        assert actual == item.expected


def test_is_this_week(date):
    value = scheddy_plus.is_this_week(date)

    return value

dict.key.subkey