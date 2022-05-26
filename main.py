import re


def encode(input):
    # regex to group sequencial matching characters using back reference
    regex = r"((.)(\2*))"
    output = ""
    # iterate the groups and build the output string
    for g in re.finditer(regex, input):
        number = len(g.group()) if len(g.group()) > 1 else ""
        output += str(number) + g.group()[-1]
    return output


def decode(input):
    # regex to group sequences of 0 or more numbers and any alpha character or whitespace
    regex = r"([0-9]*[A-Za-z ]{1})"
    output = ""
    # iterate the groups and build the output string
    for g in re.finditer(regex, input):
        total_chars = len(g.group())
        times = g.group()[:-1] if total_chars > 1 else 1
        output += g.group()[-1] * int(times)
    return output
