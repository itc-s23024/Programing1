import time


def show_how_it_begin_end(func):
    def deco_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return deco_func


def sleep_for_a_while():
    print("sleeping,,,")
    time.sleep(2)
    print("Donesleeping")


sleep_for_a_while()
