#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)

    if x == 0:
        first = None
    else:
        first = sentence[0]

    return x, first
