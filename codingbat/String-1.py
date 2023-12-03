def hello_name(name):
    return f"Hello {name}!"


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


def make_out_word(out, word):
    return out[: len(out) / 2] + word + out[len(out) / 2 :]


def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]


def first_two(str):
    return str[:2]


def first_half(str):
    return str[: len(str) / 2]


def without_end(str):
    return str[1 : len(str) - 1]


def combo_string(a, b):
    return a + b + a if len(a) < len(b) else b + a + b


def non_start(a, b):
    return a[1:] + b[1:]


def left2(str):
    return str[2:] + str[:2]
