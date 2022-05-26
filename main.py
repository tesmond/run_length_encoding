import re


def encode(input):
    regex = r"((.)(\2*))"
    output = ""
    for g in re.finditer(regex, input):
        number = len(g.group()) if len(g.group()) > 1 else ""
        output += str(number) + g.group()[-1]
    return output


def decode(input):
    regex = r"([0-9]*[A-Za-z ]{1})"
    output = ""
    for g in re.finditer(regex, input):
        total_chars = len(g.group())
        times = g.group()[:-1] if total_chars > 1 else 1
        output += g.group()[-1] * int(times)
    return output
