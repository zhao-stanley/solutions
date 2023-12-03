def string_times(str, n):
    final = ""
    for _ in range(n):
        final += str
    return final


def front_times(str, n):
    final = ""
    for _ in range(n):
        final += str[:3]
    return final


def string_bits(str):
    final = ""
    for i, char in enumerate(str):
        if i % 2 != 0:
            final += char
    return final


def string_splosion(str):
    final = ""
    for i, _ in enumerate(str):
        final += str[: i + 1]
    return final


def last2(str):
    count = 0
    for i in range(0, len(str) - 2):
        if str[i : i + 2] == str[-2:]:
            count += 1
    return count


def array_count9(nums):
    return len([n for n in nums if n == 9])


def array_front9(nums):
    return True if 9 in nums[:4] else False


def array123(nums):
    for i in range(0, len(nums) - 2):
        if nums[i : i + 3] == [1, 2, 3]:
            return True
    return False


def string_match(a, b):
    count = 0
    for i in range(0, len(a) - 1):
        if a[i : i + 2] == b[i : i + 2]:
            count += 1
    return count
