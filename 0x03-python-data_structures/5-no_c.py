#!/usr/bin/env python3
def no_c(my_string):
    cp = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(cp))
