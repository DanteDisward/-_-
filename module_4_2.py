def test_function():
    inner_function()


def inner_function():
    def print_str():
        print("Я в области видимости функции test_function")

    print_str()


test_function()
inner_function()
