#!usr/bin/env python3


def fizz_buzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "fizz_buzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return (value % mod) == 0


def check_fizz_buzz(value, expected_value):
    assert fizz_buzz(value) == expected_value


def test_returns_1_with_1_passed_in():
    check_fizz_buzz(1, "1")


def test_returns_2_with_2_passed_in():
    check_fizz_buzz(2, "2")


def test_returns_fizz_with_3_passed_in():
    check_fizz_buzz(3, "Fizz")


def test_returns_buzz_with_5_passed_in():
    check_fizz_buzz(5, "Buzz")


def test_returns_fizz_with_6_passed_in():
    check_fizz_buzz(6, "Fizz")


def test_returns_buzz_with_10_passed_in():
    check_fizz_buzz(10, "Buzz")


def test_returns_fizz_buzz_with_15_passed_in():
    check_fizz_buzz(15, "fizz_buzz")