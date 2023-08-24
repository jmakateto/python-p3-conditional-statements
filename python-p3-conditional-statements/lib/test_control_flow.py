from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

def test_admin_login():
    assert admin_login("sudo", "12345") == "Access denied"
    assert admin_login("admin", "12345") == "Access granted"
    assert admin_login("ADMIN", "12345") == "Access granted"

def test_hows_the_weather():
    assert hows_the_weather(33) == "It's brisk out there!"
    assert hows_the_weather(99) == "It's too dang hot out there!"
    assert hows_the_weather(75) == "It's perfect out there!"

def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

def test_calculator():
    assert calculator("+", 1, 1) == 2
    assert calculator("-", 3, 1) == 2
    assert calculator("*", 3, 2) == 6
    assert calculator("/", 4, 2) == 2
    assert calculator("nope", 4, 2) == "Invalid operation!"
