#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        list_keys = a_dictionary.keys()
        best_score = 0
        best_student = ""
        for key in list_keys:
            if a_dictionary[key] > best_score:
                best_score = a_dictionary[key]
                best_student = key
    else:
        best_student = None
    return best_student
