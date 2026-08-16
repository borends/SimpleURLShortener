ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)


def encode(number: int) -> str:
    if number == 0:
        return ALPHABET[0]

    result = ""

    while number > 0:
        number, remainder = divmod(number, BASE)
        result = ALPHABET[remainder] + result

    return result


def decode(code: str) -> int:
    number = 0

    for char in code:
        number = number * BASE + ALPHABET.index(char)

    return number
