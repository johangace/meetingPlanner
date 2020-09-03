from datetime import datetime

now = str(datetime.now())


def addTimeStamp(function):
    def newFunction(string):
        return function(string) + "  " + now

    return newFunction


def uppercase(string):
    return string.upper()


@addTimeStamp
def log(string):
    return " Log " + string


print(log("Hello World"))
