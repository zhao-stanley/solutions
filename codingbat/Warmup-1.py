def sleep_in(weekday, vacation):
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)


def diff21(n):
    return 2 * (n - 21) if n > 21 else 21 - n


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def makes10(a, b):
    return a + b == 10 or a == 10 or b == 10


def near_hundred(n):
    return abs(200 - n) <= 10 or abs(100 - n) <= 10


def pos_neg(a, b, negative):
    return a < 0 and b < 0 if negative else (a > 0 and b < 0) or (a < 0 and b > 0)


def not_string(str):
    return str if str[0:3] == "not" else "not " + str


def missing_char(str, n):
    return str[0:n] + str[n + 1 :]


def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


def front3(str):
    return str[0:3] + str[0:3] + str[0:3]
