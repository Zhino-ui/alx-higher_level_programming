#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        m_value = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == m_value:
                return key
    return None
