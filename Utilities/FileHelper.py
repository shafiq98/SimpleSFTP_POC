from typing import List


def divide_list_by_substring(lst: List[str], substring: str) -> List[List[str]]:
    contains_substring: List[str] = []
    does_not_contain_substring: List[str] = []

    for string in lst:
        if substring in string:
            contains_substring.append(string)
        else:
            does_not_contain_substring.append(string)

    return [contains_substring, does_not_contain_substring]


def getMostRecentFiles(file_list: list[str], substring: str) -> list[str]:
    nested_list = divide_list_by_substring(file_list, substring)
    if len(nested_list) != 2:
        raise ValueError("Nested List Length != 2")
    inpatient_list = nested_list[0]
    outpatient_list = nested_list[1]

    if len(inpatient_list) < 1 or len(outpatient_list) < 1:
        raise ValueError("Please check the length of inpatient & outpatient list")

    inpatient_list = sorted(inpatient_list, reverse=True)
    outpatient_list = sorted(outpatient_list, reverse=True)

    return [inpatient_list[0], outpatient_list[0]]