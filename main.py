import re


def encode(input: str) -> str:
    # regex to group sequencial matching characters using back reference
    regex = r"((.)(\2*))"
    output: str = ""
    # iterate the groups and build the output string
    for g in re.finditer(regex, input):
        group: str = g.group()
        number: str = str(len(group)) if len(group) > 1 else ""
        output += number + group[-1]
    return output


def decode(input: str) -> str:
    # regex to group sequences of 0 or more digits and any non-digit character
    regex = r"([\d]*[\D]{1})"
    output: str = ""
    # iterate the groups and build the output string
    for g in re.finditer(regex, input):
        group: str = g.group()
        times: int = int(group[:-1]) if len(group) > 1 else 1
        output += group[-1] * times
    return output
