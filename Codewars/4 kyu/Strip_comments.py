"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
"""


def solution(string, markers):
    string = string.split('\n')
    final_string = []
    for every_string in string:
        for symbol in every_string:
            if symbol in markers:
                place = every_string.find(symbol)
                every_string = every_string[:place].rstrip()
        final_string.append(every_string)
    return '\n'.join(final_string)
