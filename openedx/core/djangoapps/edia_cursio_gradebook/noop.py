class NoopAtomic:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, _type, _value, _traceback):
        pass


def outer_atomic():
    return NoopAtomic()


