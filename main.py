def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


def version():
    return "1.0"


def status():
    return "ok"


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
    print(version())
    print(status())
