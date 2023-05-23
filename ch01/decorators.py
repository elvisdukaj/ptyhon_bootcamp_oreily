def response_to_mailman(func):
    def wrapper():
        print("a mail man is coming")
        func()

    return wrapper

def bark():
    print("woof")


def cat_response():
    print("miaow")


bark()


response = response_to_mailman(bark)
response()

@response_to_mailman
def decorated_bark():
    print("woof")

decorated_bark()
